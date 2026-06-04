import os
import glob
import re

html_files = glob.glob('*.html')

cities = [
    "landau", "neustadt", "speyer", "karlsruhe", "weissenburg", 
    "frankenthal", "bad-duerkheim", "pforzheim", "kaiserslautern"
]

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We only want to replace the links in the navigation dropdowns.
    # The links look like: href="/bodenarbeiten-landau.html"
    # Let's replace them with href="/schreiner-landau.html"
    
    # But ONLY in the navigation block. To be safe, we can just replace all occurrences of 
    # href="/bodenarbeiten-city.html" with href="/schreiner-city.html"
    # because they only exist in the nav anyway.
    
    for city in cities:
        content = content.replace(f'href="/bodenarbeiten-{city}.html"', f'href="/schreiner-{city}.html"')
    
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")
