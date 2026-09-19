import os
import requests
from bs4 import BeautifulSoup
import time

class DocumentFetcher:
    """
    Handles fetching and cleaning HTML documents from given URLs.
    Includes retry logic and basic anti-bot headers.
    """
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }

    def fetch_html(self, url, retries=3):
        """Fetches the HTML content of the URL with retries."""
        for attempt in range(retries):
            try:
                print(f"Fetching {url} (Attempt {attempt+1}/{retries})...")
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.content
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                if attempt < retries - 1:
                    time.sleep(2)
        return None

    def parse_and_clean(self, html_content):
        """Extracts meaningful text from HTML while removing noise."""
        if not html_content:
            return ""
            
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove noisy elements
        for element in soup(["script", "style", "header", "footer", "nav", "aside", "noscript", "meta", "link"]):
            element.extract()
            
        # Return the cleaned HTML string instead of pure text
        return str(soup)

    def fetch_and_save_html(self, url, filename):
        """Fetches URL, cleans it, and saves the HTML to a file."""
        html = self.fetch_html(url)
        clean_html = self.parse_and_clean(html)
        
        if clean_html:
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(clean_html)
            print(f"Saved {len(clean_html)} characters to {filepath}")
            return clean_html
        else:
            print(f"Failed to extract HTML for {url}")
            return None
