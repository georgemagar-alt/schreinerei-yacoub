import urllib.request
import re
from bs4 import BeautifulSoup

URLS = [
    'https://yacoub-schreinerei.de/moebelbau-landau',
    'https://yacoub-schreinerei.de/innenausbau-landau',
    'https://yacoub-schreinerei.de/holzmoebel-restauration-landau',
    'https://yacoub-schreinerei.de/massanfertigungen-landau'
]

for url in URLS:
    print(f"=== SCRAPING: {url} ===")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            
            # Print title
            print("TITLE:", soup.title.string if soup.title else "No Title")
            
            # Extract H1 and H2s
            h1 = soup.find('h1')
            print("H1:", h1.get_text(strip=True) if h1 else "No H1")
            
            h2s = soup.find_all('h2')
            print("H2s:", [h2.get_text(strip=True) for h2 in h2s])
            
            # Extract image URLs
            img_urls = re.findall(r'<img[^>]+src="([^">]+)"', html)
            print("IMAGES:", len(img_urls))
            
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    print("\n")

