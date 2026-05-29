import glob

files = glob.glob('*.html')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Desktop Nav
    content = content.replace(
        '<a href="#" class="block px-4 py-2 hover:bg-[#ae8f73] hover:text-white transition-colors duration-200">Türen & Fenster</a>',
        '<a href="/tueren-fenster" class="block px-4 py-2 hover:bg-[#ae8f73] hover:text-white transition-colors duration-200">Türen & Fenster</a>'
    )
    # Mobile Nav
    content = content.replace(
        '<a href="#" class="block text-gray-400 hover:text-[#ae8f73] transition-colors duration-300">Türen & Fenster</a>',
        '<a href="/tueren-fenster" class="block text-gray-400 hover:text-[#ae8f73] transition-colors duration-300">Türen & Fenster</a>'
    )
    
    with open(file, 'w') as f:
        f.write(content)

