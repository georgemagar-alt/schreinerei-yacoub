from PIL import Image
import os

source_path = '/Users/georgemagar/.gemini/antigravity-ide/brain/129d784f-fddd-47d7-bfca-8d408d3be38e/media__1780088661398.jpg'
dest_path = '/Users/georgemagar/Desktop/Antigravity/Schreinerei Yacoub/assets/images/parkett-pflegen-schleifen.jpg'

try:
    img = Image.open(source_path)
    
    # Convert to RGB if it's not
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    # Resize if too large (max width 1200px for web articles/tiles)
    max_width = 1200
    if img.width > max_width:
        ratio = max_width / float(img.width)
        new_height = int((float(img.height) * float(ratio)))
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
    # Save optimized
    img.save(dest_path, 'JPEG', quality=80, optimize=True, progressive=True)
    print(f"Image optimized and saved to {dest_path}")
    
except Exception as e:
    print(f"Error: {e}")
