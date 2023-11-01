
"""
api_consumer.py

Task:
Fetch and print data from a specified web-API (default: 'https://jsonplaceholder.typicode.com/posts').

Extensive Details:
- The script uses the `requests` library to send a GET request to the specified API endpoint.
- The `json()` method of the response object is used to decode the returned JSON data into a Python data structure.
- The data is then printed to the console, with the first 5 items being pretty-printed for readability.

"""

import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_api_data(api_url=API_URL):
    """
    Fetch data from an API endpoint and return it as a Python data structure.

    This function sends a GET request to the provided URL, which is expected to be an API endpoint.
    The function then waits for a response from the server. Once the response is received, the function decodes the response
    body from JSON and returns the resulting data.

    Args:
    - api_url (str): The URL of the API endpoint. This should be a string containing a valid URL.

    Returns:
    - dict or list: Decoded data from the API. The type and structure of this data will depend on the specific API endpoint that was called.
    """

    try:
        # Send a GET request to the API endpoint.
        response = requests.get(api_url)

        # Check if the request was successful.
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    else:
        # Decode the response body from JSON and return the resulting data.
        return response.json()


def test_fetch_api_data(api_url=API_URL):
    """
    Test the fetch_api_data function.

    This function tests the fetch_api_data function with a known API endpoint and checks if the returned data is as expected.
    The API endpoint used for testing is 'https://jsonplaceholder.typicode.com/posts', a public API provided by JSONPlaceholder.
    The '/posts' endpoint returns a list of 100 fake blog posts in JSON format.

    """

    # Call the fetch_api_data function with the known API endpoint.
    data = fetch_api_data(api_url)

    # Check if the returned data is a list, as expected.
    assert isinstance(
        data, list
    ), f"Expected a list of blog posts; received a data structure of: {type(data)}"

    print("Test passed!")


if __name__ == "__main__":
    test_fetch_api_data()
    data = fetch_api_data()
    if data is not None:
        print(json.dumps(data[:5], indent=4))  # Pretty-print the first 5 items.
    else:
        print("Failed to fetch data from the API!")
