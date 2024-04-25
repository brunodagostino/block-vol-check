import logging
import sys

import hydra
from omegaconf import DictConfig, OmegaConf
from termcolor import colored

from csv_exporter import export_to_csv
from oci_helper import (filter_volumes_without_policy,
                        get_volume_backup_policy_assignment,
                        list_block_volumes, list_boot_volumes, load_oci_config)

# Check Python version
if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
    raise Exception("This script requires Python 3.6 or later")

# Set up logging
logger = logging.getLogger(__name__)


@hydra.main(config_path="../config", config_name="config")
def main(cfg: DictConfig) -> None:
    # Check for missing parameters
    if not cfg.block_vol_check.compartment_id:
        logger.error(
            "Compartment ID is missing. Please provide the compartment ID.")
        return

    if not cfg.block_vol_check.config_file:
        logger.error(
            "OCI configuration file path is missing. Please provide the path to your OCI configuration file.")
        return

    # Load OCI config
    config = load_oci_config(cfg.block_vol_check.config_file)
    compartment_id = cfg.block_vol_check.compartment_id

    # List boot volumes
    boot_volumes = list_boot_volumes(config, compartment_id)

    # List block volumes
    block_volumes = list_block_volumes(config, compartment_id)

    # Get volume backup policy assignments
    volume_assignments = {}

    for volume in block_volumes + boot_volumes:
        policy_assignment = get_volume_backup_policy_assignment(
            config, volume.id)

        if policy_assignment:
            volume_assignments[volume.id] = True

    # Filter block volumes without backup policy
    volumes_without_policy = filter_volumes_without_policy(
        block_volumes + boot_volumes, volume_assignments)

    # Output results
    if volumes_without_policy:
        logger.warning("Volumes without backup policy:")

        for volume in volumes_without_policy:
            logger.warning(
                f"Volume Name: {volume.display_name}, Volume ID: {volume.id}")

        # Export to CSV if filename is provided
        if cfg.block_vol_check.output_csv:
            export_to_csv(
                volumes_without_policy, cfg.block_vol_check.output_csv)
            logger.info(
                f"Exported results to {cfg.block_vol_check.output_csv}")
    else:
        logger.info("No volumes without backup policy found.")


if __name__ == "__main__":
    main()
