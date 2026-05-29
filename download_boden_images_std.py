import os
import urllib.request
import re
import urllib.parse

URL = 'https://yacoub-schreinerei.de/bodenarbeiten-landau'
IMAGE_DIR = 'assets/images'

req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
except Exception as e:
    print("Failed to fetch HTML:", e)
    exit(1)

# Basic regex to find img src
img_urls = re.findall(r'<img[^>]+src="([^">]+)"', html)

downloaded = []

for src in img_urls:
    img_url = urllib.parse.urljoin(URL, src)
    if not img_url.startswith('http'):
        continue
        
    filename = os.path.basename(urllib.parse.urlparse(img_url).path)
    if not filename or filename in ['logo.png', 'logo-white.png', 'logo-gold.png']:
        continue
        
    # Ignore SVGs
    if filename.endswith('.svg'):
        continue
        
    if filename in downloaded:
        continue
        
    print(f"Downloading {filename}...")
    
    save_name = f"boden_{filename}"
    filepath = os.path.join(IMAGE_DIR, save_name)
    
    try:
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        downloaded.append(filename)
        print(f"Saved {save_name} (Size: {len(data)} bytes)")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")

