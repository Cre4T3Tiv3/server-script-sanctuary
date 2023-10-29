#!/usr/bin/env python3

"""
file_parser.py

Task:
Parse a file with data rows, filter out invalid entries, and write the valid entries to a new file.

Extensive Details:
- We define the `filter_and_write` function which is responsible for filtering data based on specific criteria and writing the results to two separate files.
- Within the function:
    - We open the source file in read mode.
    - For each line in the source file, we attempt to split it into its constituent parts.
    - If the line matches our criteria for being valid, it's added to the valid_entries list. Otherwise, it's considered invalid and added to the invalid_entries list.
    - After processing all lines, we write valid entries to the `valid_file_path` and invalid entries to the `invalid_file_path`.

Usage:
Run this script and use the `filter_and_write` function, providing the necessary paths for the source, valid, and invalid files.
"""


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
    with open(source_file_path, "r") as file:
        valid_entries = []
        invalid_entries = []

        # Process each line in the source file
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
