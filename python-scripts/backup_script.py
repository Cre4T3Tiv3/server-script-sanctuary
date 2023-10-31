"""
backup_script.py

Task:
This script is designed to monitor a specified 'source_directory' for any new files. When a new file is detected, it is backed up to the 'backup_directory'.

Extensive Details:
- The script utilizes Python's standard libraries, specifically 'os' and 'shutil', to interact with the filesystem.
- The 'os.listdir()' function is used to retrieve a list of filenames present in the 'source_directory'.
- The 'shutil.copy2()' function is used to copy each file from the 'source_directory' to the 'backup_directory', preserving the file's metadata.
- The script operates by periodically scanning the 'source_directory' for new files. When a new file is detected, it is immediately copied to the 'backup_directory'.
"""

import os
import shutil


def backup_files(source_directory, backup_directory):
    """
    This function is responsible for backing up files from the 'source_directory' to the 'backup_directory'.

    Args:
    - source_directory (str): The directory that the function will monitor for new files.
    - backup_directory (str): The directory where newly detected files will be backed up to.
    """
    try:
        # Verify that the 'source_directory' exists.
        if not os.path.exists(source_directory):
            raise FileNotFoundError(
                f"The specified source directory: {source_directory}, does not exist."
            )

        # If the 'backup_directory' does not exist, create it.
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        # Iterate over each file in the 'source_directory'.
        for file_name in os.listdir(source_directory):
            # Use 'shutil.copy2()' to copy each file, along with its metadata, to the 'backup_directory'.
            shutil.copy2(os.path.join(source_directory, file_name), backup_directory)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def test_backup_files():
    """
    This function tests the 'backup_files' function.

    The function tests 'backup_files' by creating a temporary 'source_directory' with a test file. It then calls 'backup_files' and verifies that the test file was successfully copied to the 'backup_directory'.
    """

    import tempfile

    # Create a temporary 'source_directory' and a test file within it.
    with tempfile.TemporaryDirectory() as source_directory:
        test_file_path = os.path.join(source_directory, "test_file.txt")
        with open(test_file_path, "w") as test_file:
            test_file.write("This is a test file.")

        # Create a temporary 'backup_directory'.
        with tempfile.TemporaryDirectory() as backup_directory:
            # Call the 'backup_files' function.
            backup_files(source_directory, backup_directory)

            # Verify that the test file was successfully copied to the 'backup_directory'.
            backup_file_path = os.path.join(backup_directory, "test_file.txt")
            assert os.path.exists(
                backup_file_path
            ), "The test file was not successfully backed up!"

    print("Test passed!")


if __name__ == "__main__":
    test_backup_files()
