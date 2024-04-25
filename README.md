# Block Volume Backup Checker

Block Volume Backup Checker is a Python application that lists block volumes and boot volumes in your Oracle Cloud Infrastructure (OCI) compartment and identifies those without backup policies assigned. It provides a convenient way to ensure that all your block volumes and boot volumes are properly backed up according to your organization's policies.

## Features

- Lists block volumes and boot volumes in an OCI compartment.
- Identifies volumes without backup policies assigned.
- Supports exporting results to a CSV file for further analysis.

## Requirements

- Python 3.x
- Oracle Cloud Infrastructure (OCI) account with appropriate permissions
- OCI configuration file with valid credentials (refer to OCI documentation for details)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/brunodagostino/block-vol-check.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, ensure that you have set up your OCI configuration file (oci_config) with valid credentials and that it is located in the config/ directory. You can specify the OCI configuration file path at runtime using the config_file parameter.

Additionally, provide the compartment ID of the OCI compartment you want to check. You can specify the compartment ID at runtime using the compartment_id parameter.

## Usage

Run the application using the following command:

```bash
python main.py block_vol_check.config_file=/path/to/oci_config block_vol_check.compartment_id=<compartment_id>
```

Replace /path/to/oci_config with the path to your OCI configuration file and <compartment_id> with the ID of the OCI compartment you want to check.

## Output

The application will output a list of block volumes and boot volumes without backup policies assigned. If any volumes are found, the application will display their names and IDs. You can also export the results to a CSV file by specifying the output_csv parameter.