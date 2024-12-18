# Rubrik Batch SharePoint Restore

This Python script uses the Rubrik SDK to automate restore jobs for protected SharePoint Online sites in a specific tenant.

## Prerequisites

- Python 3.x
- [Rubrik SDK for Python](https://github.com/rubrikinc/rubrik-sdk-for-python)
- Rubrik cluster with SharePoint Online sites protected

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/teleman1991/rubrik-batch-restore.git
   ```

2. Install the Rubrik SDK:
   
   ```
   pip install rubrik_cdm
   ```

## Usage

1. Open `batch_sharepoint_restore.py` in a text editor

2. Replace `'my.rubrik.cluster'` with the IP address or hostname of your Rubrik cluster

3. Verify the `SHAREPOINT_TENANT` variable matches your SharePoint Online tenant domain

4. Save the file

5. Run the script:

   ```
   python batch_sharepoint_restore.py
   ```

The script will:
- Connect to the specified Rubrik cluster
- Retrieve a list of all protected SharePoint Online sites 
- Filter the sites to only those in the specified tenant
- Trigger a restore job for each matching site
- Print the status of each restore job

## Notes

- The user running the script must have permission in Rubrik to list and restore SharePoint sites
- Restore jobs are triggered asynchronously and the script will not wait for restores to complete
- Check the Rubrik UI for the status of the restore jobs
- Only sites matching the `SHAREPOINT_TENANT` variable will be restored

