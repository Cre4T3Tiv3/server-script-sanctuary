#!/usr/bin/env python3

"""
website_uptime_checker.py

Task:
Check if 'https://www.example.com' is accessible and print the status.

Extensive Comments:
- The script uses Python's `requests` library to send a GET request to the specified website.
- The `status_code` attribute of the response object provides the HTTP status code.
- A status code of 200 indicates that the request was successful, implying that the website is up and running.
- Any other status code suggests potential issues with the website.
"""

import requests


def check_website_status(url):
    """
    Check the status of a website by sending a GET request.

    Args:
    - url (str): The URL of the website to check.

    Returns:
    - str: A message indicating whether the website is up or down.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return "Website is up!"
    else:
        return "Website is down!"
