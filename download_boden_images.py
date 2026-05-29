import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
from PIL import Image
import io

URL = 'https://yacoub-schreinerei.de/bodenarbeiten-landau'
IMAGE_DIR = 'assets/images'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
img_tags = soup.find_all('img')

downloaded = []

for img in img_tags:
    src = img.get('src')
    if not src:
        continue
        
    img_url = urllib.parse.urljoin(URL, src)
    if not img_url.startswith('http'):
        continue
        
    try:
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        
        # Determine filename based on original URL
        filename = os.path.basename(urllib.parse.urlparse(img_url).path)
        if not filename or filename in ['logo.png', 'logo-white.png', 'logo-gold.png']:
            continue
            
        if filename in downloaded:
            continue
            
        print(f"Downloading {filename}...")
        
        # Optimize image for web using PIL
        image = Image.open(io.BytesIO(img_response.content))
        
        # Convert to RGB if necessary
        if image.mode in ('RGBA', 'P'):
            image = image.convert('RGB')
            
        # Resize if very large (max 1200px width for portfolio images)
        if image.width > 1200:
            ratio = 1200.0 / image.width
            new_height = int(image.height * ratio)
            image = image.resize((1200, new_height), Image.Resampling.LANCZOS)
            
        # Save as optimized JPEG
        save_name = f"boden_{filename}"
        if not save_name.endswith('.jpg') and not save_name.endswith('.jpeg'):
            save_name = save_name.rsplit('.', 1)[0] + '.jpg'
            
        filepath = os.path.join(IMAGE_DIR, save_name)
        image.save(filepath, 'JPEG', quality=85, optimize=True)
        downloaded.append(filename)
        print(f"Saved optimized {save_name}")
        
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")

