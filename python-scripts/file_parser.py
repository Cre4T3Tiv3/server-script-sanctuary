
"""
file_parser.py

Task: 
This script is designed to parse a file located at 'source_file_path' which contains data rows. It filters out invalid entries and writes the valid entries to a file located at 'valid_file_path'. Invalid entries are written to a file at 'invalid_file_path'.

Extensive Details:
- The script uses Python's standard libraries to interact with the filesystem and process the text data.
- The built-in 'open()' function is used to read the source file and write to the output files.
- The 'str.split()' method is used to divide each line into its constituent parts.
- The script filters data by checking each line against a defined criteria. If a line matches the criteria, it's considered valid; otherwise, it's considered invalid.
- The valid and invalid entries are stored in separate lists and then written to their respective files. 
"""

import os


def filter_and_write(valid_file_path, invalid_file_path, source_file_path):
    """
    This function filters valid and invalid entries from the source file and writes them to their respective files.

    Args:
    - valid_file_path (str): The path to the file where valid entries will be written.
    - invalid_file_path (str): The path to the file where invalid entries will be written.
    - source_file_path (str): The path to the source file that contains the data rows.

    Details:
    The function reads the source file line by line. Each line is split based on the comma delimiter.
    Lines with three non-empty segments are considered valid, and others are considered invalid.
    """
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(
            f"The specified source file: {source_file_path}, does not exist."
        )

    valid_entries = []
    invalid_entries = []

    with open(source_file_path, "r") as file:
        valid_entries = []
        invalid_entries = []
        # Process each line in the source file.
        for line in file:
            data = line.strip().split(",")
            if len(data) == 3 and all(
                data
            ):  # Check if the line has three non-empty segments.
                valid_entries.append(line)
            else:
                invalid_entries.append(line)

    # Write the valid entries to the valid file.
    with open(valid_file_path, "w") as valid_file:
        valid_file.writelines(valid_entries)

    # Write the invalid entries to the invalid file.
    with open(invalid_file_path, "w") as invalid_file:
        invalid_file.writelines(invalid_entries)


def test_filter_and_write():
    """
    This function tests the 'filter_and_write' function.

    The function tests 'filter_and_write' by creating a temporary source file with test data. It then calls 'filter_and_write' and verifies that the valid and invalid entries were correctly filtered and written.
    """

    import tempfile

    # Create a temporary source file with test data.
    with tempfile.NamedTemporaryFile(delete=False) as source_file:
        source_file.write(b"valid1,valid2,valid3\ninvalid1,invalid2\n")

    # Create temporary files for valid and invalid entries.
    with tempfile.NamedTemporaryFile(
        delete=False
    ) as valid_file, tempfile.NamedTemporaryFile(delete=False) as invalid_file:
        # Call the 'filter_and_write' function.
        filter_and_write(valid_file.name, invalid_file.name, source_file.name)

        # Verify that the valid and invalid entries were correctly filtered and written.
        with open(valid_file.name, "r") as valid_file_check, open(
            invalid_file.name, "r"
        ) as invalid_file_check:
            assert (
                valid_file_check.read() == "valid1,valid2,valid3\n"
            ), "Valid entries were not correctly written to the file."
            assert (
                invalid_file_check.read() == "invalid1,invalid2\n"
            ), "Invalid entries were not correctly written to the file."

    print("Test passed!")


if __name__ == "__main__":
    test_filter_and_write()
