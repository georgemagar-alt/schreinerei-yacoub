import os
import urllib.request
import re
import urllib.parse
import json
from bs4 import BeautifulSoup

PAGES = [
    {'url': 'https://yacoub-schreinerei.de/moebelbau-landau', 'prefix': 'moebelbau'},
    {'url': 'https://yacoub-schreinerei.de/innenausbau-landau', 'prefix': 'innenausbau'},
    {'url': 'https://yacoub-schreinerei.de/holzmoebel-restauration-landau', 'prefix': 'restauration'},
    {'url': 'https://yacoub-schreinerei.de/massanfertigungen-landau', 'prefix': 'massanfertigung'}
]

IMAGE_DIR = 'assets/images'
data_store = {}

for page in PAGES:
    url = page['url']
    prefix = page['prefix']
    print(f"Processing {prefix}...")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print("Failed to fetch HTML:", e)
        continue
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Save text content
    text_content = []
    for string in soup.stripped_strings:
        if len(string) > 20:
            text_content.append(string)
    
    data_store[prefix] = {
        'title': soup.title.string if soup.title else '',
        'text': text_content,
        'images': []
    }
    
    # Download images
    img_urls = re.findall(r'<img[^>]+src="([^">]+)"', html)
    counter = 1
    downloaded = []
    
    for src in img_urls:
        img_url = urllib.parse.urljoin(url, src)
        if not img_url.startswith('http'): continue
            
        filename = os.path.basename(urllib.parse.urlparse(img_url).path)
        if not filename or filename in ['logo.png', 'logo-white.png', 'logo-gold.png'] or filename.endswith('.svg') or 'map' in filename.lower():
            continue
            
        if filename in downloaded: continue
            
        save_name = f"{prefix}-{counter}.jpeg"
        filepath = os.path.join(IMAGE_DIR, save_name)
        
        try:
            req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_img) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            data_store[prefix]['images'].append(save_name)
            downloaded.append(filename)
            print(f"  Saved {save_name}")
            counter += 1
        except Exception as e:
            print(f"  Failed to download {img_url}: {e}")

with open('scraped_data.json', 'w') as f:
    json.dump(data_store, f, indent=2, ensure_ascii=False)

