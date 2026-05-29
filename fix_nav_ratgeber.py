import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop Nav Replacement
    # The actual HTML is:
    # <a href="#warum-wir" class="block py-3 text-white uppercase tracking-widest text-sm hover:text-[#ae8f73] transition-colors relative group">
    #     Warum wir
    content = re.sub(
        r'<a href="(?:/)?#warum-wir" class="(block py-3 text-white uppercase tracking-widest text-sm hover:text-\[#ae8f73\] transition-colors relative group)">\s*Warum wir',
        r'<a href="/ratgeber.html" class="\1">\n                        Ratgeber',
        content
    )

    # Mobile Nav Replacement
    content = re.sub(
        r'<a href="(?:/)?#warum-wir" class="(block py-3 text-white uppercase tracking-widest text-sm hover:text-\[#ae8f73\] border-b border-white/5 transition-colors)">Warum wir</a>',
        r'<a href="/ratgeber.html" class="\1">Ratgeber</a>',
        content
    )

    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")

