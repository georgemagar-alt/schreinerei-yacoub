import os
import glob
import re

html_files = glob.glob('*.html')

cities = [
    "landau", "neustadt", "speyer", "karlsruhe", "weissenburg", 
    "frankenthal", "bad-duerkheim", "pforzheim", "kaiserslautern"
]

def replace_in_nav(match):
    nav_content = match.group(0)
    for city in cities:
        nav_content = nav_content.replace(f'href="/bodenarbeiten-{city}.html"', f'href="/schreiner-{city}.html"')
    return nav_content

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We want to replace inside <nav ...> ... </nav>
    # Using re.sub with a function
    content = re.sub(r'<nav.*?</nav>', replace_in_nav, content, flags=re.DOTALL)
    
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")
