# parser.py

from bs4 import BeautifulSoup

def extract_data(soup, url):
    """Extracts page title, text, and image URLs."""
    title = soup.title.text if soup.title else "No Title"
    text = " ".join([p.text.strip() for p in soup.find_all("p")])
    images = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]

    return {
        "url": url,
        "title": title,
        "text": text[:500],  # Limit text length
        "images": images
    }
