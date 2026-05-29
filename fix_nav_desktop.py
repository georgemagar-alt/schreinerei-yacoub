import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop Nav Replacement (Catches anything that ends in >Warum wir</a> and has href="#warum-wir" or href="/#warum-wir")
    content = re.sub(
        r'<a href="(?:/)?#warum-wir"([^>]*)>\s*Warum wir\s*</a>',
        r'<a href="/ratgeber.html"\1>Ratgeber</a>',
        content
    )

    # There might be cases where 'Warum wir' is not the only thing in the tag.
    # Let's also do a simple replace just in case:
    content = content.replace('href="#warum-wir"', 'href="/ratgeber.html"')
    content = content.replace('href="/#warum-wir"', 'href="/ratgeber.html"')
    content = content.replace('>Warum wir</a>', '>Ratgeber</a>')

    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")

