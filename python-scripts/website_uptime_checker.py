"""
website_uptime_checker.py

Task:
Check if 'https://www.example.com' is accessible and print the status.

Extensive Details:
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
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "The website is up!"
        else:
            return "The website is down!"
    except requests.exceptions.RequestException as err:
        return f"The following error occurred: {err}"
    except Exception as e:
        return f"The following unexpected error occurred: {str(e)}"


def test_check_website_status():
    """
    Test the check_website_status function.

    This function tests the check_website_status function by checking the status of 'https://www.example.com'.
    """

    # Call the check_website_status function.
    status = check_website_status("https://www.example.com")

    # Check if the status is as expected.
    assert status in [
        "The website is up!",
        "The website is down!",
    ], "An unexpected status message."

    print("Test passed!")


if __name__ == "__main__":
    test_check_website_status()
    print(check_website_status("https://www.example.com"))
