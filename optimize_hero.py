from PIL import Image
import os

input_path = "assets/images/hero-image-homepage.jpeg"
output_path = "assets/images/schreinerei-yacoub-moebelbau-massgefertigt.jpeg"

if not os.path.exists(input_path):
    print("Input image not found!")
else:
    img = Image.open(input_path)
    
    # Resize to max 1920px width if larger
    if img.width > 1920:
        ratio = 1920.0 / img.width
        new_height = int(img.height * ratio)
        img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
    
    # Save optimized
    img.save(output_path, "JPEG", optimize=True, quality=80)
    print(f"Optimized image saved to {output_path}")
