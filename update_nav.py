import re

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update Desktop Nav
    old_desktop_nav = """<a href="#leistungen" class="text-sm font-medium uppercase tracking-widest hover:text-[#ae8f73] transition-colors relative py-2 after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-0 after:h-[2px] after:bg-[#ae8f73] hover:after:w-full after:transition-all after:duration-300">Leistungen</a>"""
    
    new_desktop_nav = """<div class="relative group">
                    <a href="/#leistungen" class="text-sm font-medium uppercase tracking-widest hover:text-[#ae8f73] transition-colors relative py-6 flex items-center gap-1 group-hover:text-[#ae8f73]">
                        Leistungen
                        <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </a>
                    <!-- Dropdown -->
                    <div class="absolute left-0 top-[100%] w-64 bg-white rounded-b-2xl shadow-2xl border-t-2 border-[#ae8f73] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform -translate-y-2 group-hover:translate-y-0 z-50 overflow-hidden">
                        <div class="py-2">
                            <a href="/bodenarbeiten.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Bodenarbeiten</a>
                            <a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Innenausbau</a>
                            <a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Möbelbau</a>
                            <a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Türen & Fenster</a>
                            <a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Maßanfertigung</a>
                            <a href="/#leistungen" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Restauration</a>
                        </div>
                    </div>
                </div>"""
                
    content = content.replace(old_desktop_nav, new_desktop_nav)
    
    # 2. Update Mobile Nav
    old_mobile_nav = """<a href="#leistungen" class="block py-3 text-white uppercase tracking-widest text-sm hover:text-[#ae8f73] border-b border-white/5 transition-colors">Leistungen</a>"""
    
    new_mobile_nav = """<div class="border-b border-white/5">
                <a href="/#leistungen" class="block py-3 text-white uppercase tracking-widest text-sm hover:text-[#ae8f73] transition-colors">Leistungen</a>
                <div class="pl-4 pb-2 space-y-2">
                    <a href="/bodenarbeiten.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Bodenarbeiten</a>
                    <a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Innenausbau</a>
                    <a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Möbelbau</a>
                    <a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Türen & Fenster</a>
                    <a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Maßanfertigung</a>
                    <a href="/#leistungen" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Restauration</a>
                </div>
            </div>"""
            
    content = content.replace(old_mobile_nav, new_mobile_nav)
    
    # 3. Fix anchors for subpages (so they go to /#warum-wir instead of #warum-wir)
    if 'bodenarbeiten.html' in filepath:
        content = content.replace('href="#warum-wir"', 'href="/#warum-wir"')
        content = content.replace('href="#region"', 'href="/#region"')
        content = content.replace('href="#kontakt"', 'href="/#kontakt"')

    # 4. Footer link for Bodenarbeiten
    old_footer_link = """<li><a href="#leistungen" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Bodenarbeiten</a></li>"""
    new_footer_link = """<li><a href="/bodenarbeiten.html" class="hover:text-[#ae8f73] transition-colors flex items-center"><span class="w-1 h-1 bg-gray-700 rounded-full mr-3"></span>Bodenarbeiten</a></li>"""
    content = content.replace(old_footer_link, new_footer_link)

    with open(filepath, 'w') as f:
        f.write(content)

update_file('index.html')
update_file('bodenarbeiten.html')
