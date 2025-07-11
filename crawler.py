# crawler.py

import requests
from bs4 import BeautifulSoup
from config import MAX_PAGES, HEADERS
from storage import save_data
from utils import get_random_user_agent

visited_urls = set()

def crawl(url, depth=0):
    """Fetch web page, extract data, and follow links."""
    if depth >= MAX_PAGES or url in visited_urls:
        return

    # Skip unsupported URL schemes like intent:, mailto:, javascript:
    if not url.startswith("http://") and not url.startswith("https://"):
        print(f"Skipping unsupported URL: {url}")
        return

    print(f"Crawling: {url}")
    visited_urls.add(url)

    headers = {"User-Agent": get_random_user_agent()}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return

    if response.status_code != 200:
        print(f"Failed to fetch {url} - Status Code: {response.status_code}")
        return

    # Parse the page
    soup = BeautifulSoup(response.content, "html.parser")

    # ✅ Extract and save page title
    title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
    data = {
        "url": url,
        "title": title
    }
    save_data(data)

    # Follow links
    links = soup.find_all("a", href=True)
    for link in links:
        next_url = link['href']

        # Skip anchors, JavaScript, mailto, intent, etc.
        if next_url.startswith('#') or next_url.startswith('mailto:') or next_url.startswith('javascript:') or next_url.startswith('intent:'):
            continue

        # Handle relative links
        if next_url.startswith('/'):
            from urllib.parse import urljoin
            next_url = urljoin(url, next_url)

        crawl(next_url, depth + 1)
