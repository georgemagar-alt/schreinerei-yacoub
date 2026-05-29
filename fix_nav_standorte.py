import glob
import re

files = glob.glob('*.html')

desktop_dropdown = """<div class="relative group">
                    <a href="#" class="text-sm font-medium uppercase tracking-widest hover:text-[#ae8f73] transition-colors relative py-2 flex items-center gap-1 group-hover:text-[#ae8f73]">
                        Standorte
                        <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </a>
                    <!-- Dropdown -->
                    <div class="absolute left-0 top-[100%] w-64 bg-white rounded-b-2xl shadow-2xl border-t-2 border-[#ae8f73] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform -translate-y-2 group-hover:translate-y-0 z-50 overflow-hidden">
                        <div class="py-2">
                            <a href="/bodenarbeiten-landau.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Landau i.d. Pfalz</a>
                            <a href="/bodenarbeiten-neustadt.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Neustadt a.d.W.</a>
                            <a href="/bodenarbeiten-speyer.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Speyer</a>
                            <a href="/bodenarbeiten-karlsruhe.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Karlsruhe</a>
                            <a href="/bodenarbeiten-weissenburg.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Weißenburg</a>
                            <a href="/bodenarbeiten-frankenthal.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Frankenthal</a>
                            <a href="/bodenarbeiten-bad-duerkheim.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Bad Dürkheim</a>
                            <a href="/bodenarbeiten-pforzheim.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Pforzheim</a>
                            <a href="/bodenarbeiten-kaiserslautern.html" class="block px-6 py-3 text-sm font-medium text-gray-800 hover:bg-[#f9f8f6] hover:text-[#ae8f73] transition-colors border-l-2 border-transparent hover:border-[#ae8f73]">Kaiserslautern</a>
                        </div>
                    </div>
                </div>"""

mobile_dropdown = """<div class="py-2 border-b border-white/5">
                <span class="block py-2 text-white uppercase tracking-widest text-sm mb-2">Standorte</span>
                <div class="pl-4 space-y-1">
                    <a href="/bodenarbeiten-landau.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Landau i.d. Pfalz</a>
                    <a href="/bodenarbeiten-neustadt.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Neustadt a.d.W.</a>
                    <a href="/bodenarbeiten-speyer.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Speyer</a>
                    <a href="/bodenarbeiten-karlsruhe.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Karlsruhe</a>
                    <a href="/bodenarbeiten-weissenburg.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Weißenburg</a>
                    <a href="/bodenarbeiten-frankenthal.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Frankenthal</a>
                    <a href="/bodenarbeiten-bad-duerkheim.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Bad Dürkheim</a>
                    <a href="/bodenarbeiten-pforzheim.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Pforzheim</a>
                    <a href="/bodenarbeiten-kaiserslautern.html" class="block py-2 text-gray-400 text-sm hover:text-[#ae8f73] transition-colors">- Kaiserslautern</a>
                </div>
            </div>"""

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop Nav Replacement
    content = re.sub(
        r'<a href="(?:/)?#region" class="[^"]*?text-sm font-medium uppercase tracking-widest hover:text-\[#ae8f73\] transition-colors relative py-2.*?(?:>|\s)Region\s*</a>',
        desktop_dropdown,
        content,
        flags=re.DOTALL
    )

    # Mobile Nav Replacement
    content = re.sub(
        r'<a href="(?:/)?#region" class="[^"]*?block py-3 text-white uppercase tracking-widest text-sm hover:text-\[#ae8f73\] border-b border-white/5 transition-colors"[^>]*>\s*Region\s*</a>',
        mobile_dropdown,
        content,
        flags=re.DOTALL
    )

    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")
