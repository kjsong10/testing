import requests
import time

def fetch_metrics(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time

        print(f"Website URL: {url}")
        print(f"HTTP Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")
    except requests.RequestException as e:
        print(f"Failed to fetch website metrics: {e}")

if __name__ == "__main__":
    # Specify the website URL
    website_url = "kjsong10.github.io/testing/"
    fetch_metrics(website_url)
