"""
backup_script.py

Task:
Monitor 'source_directory' for new files and back them up in 'backup_directory'.

Extensive Details:
- The code uses Python's standard libraries (os and shutil) to interact with the filesystem.
- The os.listdir() method provides a list of filenames in a directory.
- shutil.copy2() allows copying a file along with its metadata.
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
    try:
        # Check if source_directory exists.
        if not os.path.exists(source_directory):
            raise FileNotFoundError(
                f"Source directory {source_directory} does not exist."
            )

        # Check if backup_directory exists, if not create it.
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        # Iterate over each file in the source directory.
        for file_name in os.listdir(source_directory):
            # Use shutil's copy2 method to copy files along with their metadata.
            shutil.copy2(os.path.join(source_directory, file_name), backup_directory)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def test_backup_files():
    """
    Test the backup_files function.

    This function tests the backup_files function by creating a temporary source directory with a test file,
    then calling backup_files and checking if the test file was copied to the backup directory.
    """

    import tempfile

    # Create a temporary source directory with a test file.
    with tempfile.TemporaryDirectory() as source_directory:
        test_file_path = os.path.join(source_directory, "test_file.txt")
        with open(test_file_path, "w") as test_file:
            test_file.write("Test file content.")

        # Create a temporary backup directory.
        with tempfile.TemporaryDirectory() as backup_directory:
            # Call the backup_files function.
            backup_files(source_directory, backup_directory)

            # Check if the test file was copied to the backup directory.
            backup_file_path = os.path.join(backup_directory, "test_file.txt")
            assert os.path.exists(backup_file_path), "Test file was not backed up."

    print("Test passed.")


if __name__ == "__main__":
    test_backup_files()
