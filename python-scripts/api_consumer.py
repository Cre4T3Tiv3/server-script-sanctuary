import argparse
import requests
import json
import logging
import os
import requests_cache

# Initialize caching.
requests_cache.install_cache("api_cache", expire_after=1800)

# Configure logging.
logging.basicConfig(
    filename="api_consumer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configure the command-line argument parser.
parser = argparse.ArgumentParser(description="Fetch data from an API endpoint.")
parser.add_argument(
    "--url",
    type=str,
    default="https://jsonplaceholder.typicode.com/posts",
    help="API endpoint URL",
)
parser.add_argument(
    "--apikey",
    type=str,
    default=os.getenv("API_KEY"),
    help="API Key for authentication",
)
parser.add_argument(
    "--timeout", type=int, default=10, help="Timeout for API request in seconds"
)
args = parser.parse_args()


def fetch_api_data(api_url, api_key=None, timeout=10):
    """
    Fetch data from an API endpoint and return it as a Python data structure.
    """
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    try:
        logging.info(f"Sending GET request to API URL: {api_url}")
        response = requests.get(api_url, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        logging.error(
            f"HTTP error occurred: {http_err} - Status Code: {http_err.response.status_code}"
        )
        return None
    except Exception as err:
        logging.error(f"Error occurred: {err}")
        return None
    else:
        logging.info("API data fetched successfully.")
        return response.json()


def display_data(data):
    """
    Display data in JSON format, pretty-printing the first 5 items.
    """
    if data:
        print(json.dumps(data[:5], indent=4))
    else:
        logging.error("No data to display.")


def main():
    api_url = args.url
    api_key = args.apikey
    timeout = args.timeout

    data = fetch_api_data(api_url, api_key, timeout)
    display_data(data)


if __name__ == "__main__":
    main()
