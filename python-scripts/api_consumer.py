#!/usr/bin/env python3

"""
api_consumer.py

Task:
Fetch and print data from 'https://api.example.com/data'.

Extensive Details:
- The script uses the `requests` library to send a GET request to the specified API endpoint.
- The `json()` method of the response object is used to parse the returned JSON data.
- The data is then printed to the console.
"""

import requests


def fetch_api_data(api_url):
    """
    Fetch data from an API endpoint and return it as a JSON object.

    Args:
    - api_url (str): The URL of the API endpoint.

    Returns:
    - dict: Parsed JSON data from the API.
    """
    response = requests.get(api_url)
    return response.json()
