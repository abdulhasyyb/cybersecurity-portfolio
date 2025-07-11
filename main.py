import sys
from crawler import crawl

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
    print(f"Starting Web Crawler for {target_url}")
    crawl(target_url)
    print("Crawling Complete! Check output.json")

if __name__ == "__main__":
    main()

