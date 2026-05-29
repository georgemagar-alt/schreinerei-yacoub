import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop Nav Bug Fix
    content = content.replace(
        '<a href="/ratgeber.html" class="text-sm font-medium uppercase tracking-widest hover:text-[#ae8f73] transition-colors relative py-2 after:content-[\'\'] after:absolute after:bottom-0 after:left-0 after:w-0 after:h-[2px] after:bg-[#ae8f73] hover:after:w-full after:transition-all after:duration-300">Ratgeber</a>\n                </div>',
        '</div>\n                <a href="/ratgeber.html" class="text-sm font-medium uppercase tracking-widest hover:text-[#ae8f73] transition-colors relative py-2 after:content-[\'\'] after:absolute after:bottom-0 after:left-0 after:w-0 after:h-[2px] after:bg-[#ae8f73] hover:after:w-full after:transition-all after:duration-300">Ratgeber</a>'
    )

    with open(file, 'w') as f:
        f.write(content)
    print(f"Fixed {file}")
