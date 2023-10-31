"""
api_consumer.py

Task:
Fetch and print data from 'https://jsonplaceholder.typicode.com/posts'.

Extensive Details:
- The script uses the `requests` library to send a GET request to the specified API endpoint.
- The `json()` method of the response object is used to parse the returned JSON data.
- The data is then printed to the console.
"""

import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_api_data(api_url=API_URL):
    """
    Fetch data from an API endpoint and return it as a JSON object.
    This function takes a URL as an argument. It sends a GET request to this URL, which is expected to be an API endpoint.
    The function then waits for a response from the server. Once the response is received, the function parses the response
    body as JSON and returns the resulting data.

    Args:
    - api_url (str): The URL of the API endpoint. This should be a string containing a valid URL.

    Returns:
    - dict: Parsed JSON data from the API. This is a dictionary that contains the data returned by the API. The structure
            of this data will depend on the specific API endpoint that was called.
    """

    try:
        # Send a GET request to the API endpoint.
        # The requests.get function takes a URL and sends a GET request to this URL. It then returns a Response object.
        # This object contains the server's response to our request.
        response = requests.get(api_url)

        # Check if the request was successful.
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        print(f"The following HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"The following error occurred: {err}")
    else:
        # Parse the response body as JSON and return the resulting data.
        # The json method of the Response object takes the response body and parses it as JSON. It then returns the resulting data.
        # If the response body does not contain valid JSON, this method will raise an error.
        return response.json()


def test_fetch_api_data(api_url=API_URL):
    """
    Test the fetch_api_data function.

    This function tests the fetch_api_data function with a known API endpoint and checks if the returned data is as expected.
    The API endpoint used for testing is 'https://jsonplaceholder.typicode.com/posts'. This is a public API provided by JSONPlaceholder.
    It's a simple fake REST API that's useful for testing and prototyping. The '/posts' endpoint returns a list of 100 fake blog posts in JSON format.
    Each post is a dictionary with the following keys: 'userId', 'id', 'title', and 'body'. 'userId' and 'id' are integers, while 'title' and 'body' are strings.
    """

    # Call the fetch_api_data function with the known API endpoint.
    data = fetch_api_data(api_url)

    # Check if the returned data is as expected.
    assert isinstance(data, list), f"Expected a list of blog posts; received a data structure of: {type(data)}"

    print("Test passed!")


if __name__ == "__main__":
    test_fetch_api_data()
    data = fetch_api_data()
    if data is not None:
        print(json.dumps(data[:5], indent=4))  # Pretty-print the first 5 items.
    else:
        print("Failed to fetch data from the website!")
