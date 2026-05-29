import glob

files = glob.glob('*.html')
for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop Dropdown
    content = content.replace('<a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Innenausbau</a>', '<a href="/innenausbau.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Innenausbau</a>')
    content = content.replace('<a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Möbelbau</a>', '<a href="/moebelbau.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Möbelbau</a>')
    content = content.replace('<a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Türen & Fenster</a>', '<a href="/tueren-fenster.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Türen & Fenster</a>')
    content = content.replace('<a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Maßanfertigung</a>', '<a href="/massanfertigung.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Maßanfertigung</a>')
    content = content.replace('<a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Restauration</a>', '<a href="/restauration.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Restauration</a>')

    # Mobile Nav
    content = content.replace('<a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Innenausbau</a>', '<a href="/innenausbau.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Innenausbau</a>')
    content = content.replace('<a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Möbelbau</a>', '<a href="/moebelbau.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Möbelbau</a>')
    content = content.replace('<a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Türen & Fenster</a>', '<a href="/tueren-fenster.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Türen & Fenster</a>')
    content = content.replace('<a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Maßanfertigung</a>', '<a href="/massanfertigung.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Maßanfertigung</a>')
    content = content.replace('<a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Restauration</a>', '<a href="/restauration.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Restauration</a>')

    # Footer Nav
    content = content.replace('<li><a href="#leistungen" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Innenausbau</a></li>', '<li><a href="/innenausbau.html" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Innenausbau</a></li>')
    content = content.replace('<li><a href="#leistungen" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Möbelbau</a></li>', '<li><a href="/moebelbau.html" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Möbelbau</a></li>')
    content = content.replace('<li><a href="#leistungen" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Türen & Fenster</a></li>', '<li><a href="/tueren-fenster.html" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Türen & Fenster</a></li>')
    content = content.replace('<li><a href="#leistungen" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Restauration</a></li>', '<li><a href="/restauration.html" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Restauration</a></li>')
    content = content.replace('<li><a href="#leistungen" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Maßanfertigung</a></li>', '<li><a href="/massanfertigung.html" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Maßanfertigung</a></li>')

    with open(file, 'w') as f:
        f.write(content)

