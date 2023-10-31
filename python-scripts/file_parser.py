"""
file_parser.py

Task:
Parse a file with data rows, filter out invalid entries, and write the valid entries to a new file.

Extensive Details:
- Define the `filter_and_write` function which is responsible for filtering data based on specific criteria and writing the results to two separate files.
- Within the function:
    - Open the source file in read mode.
    - For each line in the source file, attempt to split it into its constituent parts.
    - If the line matches our criteria for being valid, it's added to the valid_entries list. Otherwise, it's considered invalid and added to the invalid_entries list.
    - After processing all lines, write valid entries to the `valid_file_path` and invalid entries to the `invalid_file_path`.

Usage:
Run this script and use the `filter_and_write` function, providing the necessary paths for the source, valid, and invalid files.
"""

import os


def filter_and_write(valid_file_path, invalid_file_path, source_file_path):
    """
    Filters valid and invalid entries from the source file and writes them to respective files.

    Args:
    - valid_file_path (str): Path to the file where valid entries will be written.
    - invalid_file_path (str): Path to the file where invalid entries will be written.
    - source_file_path (str): Path to the source file containing data rows.

    Details:
    The function reads the source file line by line. Each line is split based on the comma delimiter.
    Lines with three non-empty segments are considered valid, and others are considered invalid.
    """
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(f"Source file: {source_file_path}, does not exist.")

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
    Test the filter_and_write function.

    This function tests the filter_and_write function by creating a temporary source file with test data,
    then calling filter_and_write and checking if the valid and invalid entries were correctly filtered and written.
    """

    import tempfile

    # Create a temporary source file with test data.
    with tempfile.NamedTemporaryFile(delete=False) as source_file:
        source_file.write(b"valid1,valid2,valid3\ninvalid1,invalid2\n")

    # Create temporary files for valid and invalid entries.
    with tempfile.NamedTemporaryFile(
        delete=False
    ) as valid_file, tempfile.NamedTemporaryFile(delete=False) as invalid_file:
        # Call the filter_and_write function.
        filter_and_write(valid_file.name, invalid_file.name, source_file.name)

        # Check if the valid and invalid entries were correctly filtered and written.
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
