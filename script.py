import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_js_links(domain):
    # Send a GET request to the domain
    response = requests.get(domain)
    if response.status_code != 200:
        print(f"Failed to retrieve the website. HTTP Status Code: {response.status_code}")
        return

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all script tags
    script_tags = soup.find_all("script")

    # List to store the JavaScript file URLs
    js_links = []

    for script in script_tags:
        # Check if 'src' attribute exists
        if script.get("src"):
            # Get the full URL 
            js_url = urljoin(domain, script["src"])
            if js_url.endswith(".js"):  # Ensure it's a JavaScript file
                js_links.append(js_url)

    # Output all found JavaScript links
    if js_links:
        print(f"JavaScript files found on {domain}:")
        for link in js_links:
            print(link)
    else:
        print(f"No JavaScript files found on {domain}.")

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Get all JavaScript file links from a website.")
    parser.add_argument("-d", "--domain", required=True, help="The domain of the website (e.g., https://domain.com)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Fetch and print the JS links from the given domain
    fetch_js_links(args.domain)

if __name__ == "__main__":
    main()

