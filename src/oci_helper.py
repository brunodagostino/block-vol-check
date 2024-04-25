import os

from oci.config import from_file
from oci.core import BlockstorageClient


def load_oci_config(config_file_path: str) -> dict:
    """
    Load OCI configuration from the specified file path.

    Args:
        config_file_path (str): Path to the OCI configuration file.

    Returns:
        dict: OCI configuration loaded from the file.
    """
    try:
        oci_config = from_file(config_file_path)

        return oci_config
    except Exception as e:
        raise RuntimeError(
            f"Failed to load OCI configuration from '{config_file_path}': {str(e)}")


def list_boot_volumes(config, compartment_id, availability_domain=None):
    # List boot volumes
    blockstorage_client = BlockstorageClient(config)
    boot_volumes = blockstorage_client.list_boot_volumes(
        compartment_id=compartment_id, availability_domain=availability_domain).data  # type: ignore

    return boot_volumes


def list_block_volumes(config, compartment_id, availability_domain=None):
    # List block volumes
    blockstorage_client = BlockstorageClient(config)
    block_volumes = blockstorage_client.list_volumes(
        compartment_id=compartment_id, availability_domain=availability_domain).data  # type: ignore

    return block_volumes


def get_volume_backup_policy_assignment(config, volume_id):
    blockstorage_client = BlockstorageClient(config)

    try:
        policy_assignment = blockstorage_client.get_volume_backup_policy_asset_assignment(
            volume_id).data  # type: ignore

        return policy_assignment
    except Exception as e:
        # Handle exception if volume doesn't have any policy assignment
        return None


def filter_volumes_without_policy(block_volumes, volume_ids):
    volumes_without_policy = [
        volume for volume in block_volumes if volume.id not in volume_ids]
    return volumes_without_policy
