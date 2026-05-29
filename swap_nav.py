import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop Nav Swap
    # We find the Ratgeber A tag and the Standorte DIV block in the desktop nav.
    pattern_desktop = re.compile(
        r'(<a href="/ratgeber\.html" class="text-sm font-medium uppercase tracking-widest hover:text-\[#ae8f73\] transition-colors relative py-2[^>]*>Ratgeber</a>)\s*(<div class="relative group">\s*<a href="#" class="text-sm font-medium uppercase tracking-widest hover:text-\[#ae8f73\] transition-colors relative py-2 flex items-center gap-1 group-hover:text-\[#ae8f73\]">.*?Standorte.*?<div class="absolute left-0 top-\[100%\] w-64 bg-white rounded-b-2xl shadow-2xl border-t-2 border-\[#ae8f73\] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform -translate-y-2 group-hover:translate-y-0 z-50 overflow-hidden">.*?</div>\s*</div>)',
        re.DOTALL
    )
    content = pattern_desktop.sub(r'\2\n                \1', content)

    # Mobile Nav Swap
    pattern_mobile = re.compile(
        r'(<a href="/ratgeber\.html" class="block py-3 text-white uppercase tracking-widest text-sm hover:text-\[#ae8f73\] border-b border-white/5 transition-colors">Ratgeber</a>)\s*(<div class="py-2 border-b border-white/5">\s*<span class="block py-2 text-white uppercase tracking-widest text-sm mb-2">Standorte</span>\s*<div class="pl-4 space-y-1">.*?</div>\s*</div>)',
        re.DOTALL
    )
    content = pattern_mobile.sub(r'\2\n            \1', content)

    with open(file, 'w') as f:
        f.write(content)
        
    print(f"Updated {file}")
