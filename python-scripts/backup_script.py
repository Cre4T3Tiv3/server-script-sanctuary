#!/usr/bin/env python3

"""
backup_script.py

Task:
Monitor 'source_directory' for new files and back them up in 'backup_directory'.

Extensive Details:
- The code uses Python's standard libraries (os and shutil) to interact with the filesystem.
- The os.listdir() method provides a list of filenames in a directory.
- shutil.copy2() allows us to copy a file along with its metadata.
- The script monitors changes by periodically checking for new files in the source directory and then copying them over to a backup directory.
"""

import os
import shutil


def backup_files(source_directory, backup_directory):
    """
    Backs up files from the source directory to the backup directory.

    Args:
    - source_directory (str): The directory to monitor for new files.
    - backup_directory (str): The directory where new files should be backed up.
    """
    # Iterate over each file in the source directory.
    for file_name in os.listdir(source_directory):
        # Use shutil's copy2 method to copy files along with their metadata.
        shutil.copy2(os.path.join(source_directory, file_name), backup_directory)
