import re

with open('index.html', 'r') as f:
    content = f.read()

# We need to wrap each service block with <a href="..."> ... </a>
# The blocks look like this:
# <!-- Service 1 -->
# <div class="bg-white rounded-xl overflow-hidden shadow-[0_4px_20px_-4px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group border border-gray-100">

# Services and their links
services = {
    "Möbelbau": "moebelbau.html",
    "Innenausbau": "innenausbau.html",
    "Türen & Fensterbau": "tueren-fenster.html",
    "Restauration": "restauration.html",
    "Maßanfertigung": "massanfertigung.html",
    "Bodenarbeiten": "bodenarbeiten.html"
}

# Iterate and replace
for s_name, link in services.items():
    if s_name == "Maßanfertigung":
        # Handle plurals in the HTML
        search_pattern = r'(<div class="bg-white rounded-xl overflow-hidden shadow-\[0_4px_20px_-4px_rgba\(0,0,0,0\.05\)\] hover:shadow-\[0_20px_40px_-10px_rgba\(0,0,0,0\.1\)\] transition-all duration-500 hover:-translate-y-2 group border border-gray-100">)(.*?<h3 class="text-xl font-bold mb-3 text-\[#242424\] group-hover:text-\[#ae8f73\] transition-colors">Maßanfertigungen</h3>.*?</div>\s*</div>)'
    else:
        search_pattern = fr'(<div class="bg-white rounded-xl overflow-hidden shadow-\[0_4px_20px_-4px_rgba\(0,0,0,0\.05\)\] hover:shadow-\[0_20px_40px_-10px_rgba\(0,0,0,0\.1\)\] transition-all duration-500 hover:-translate-y-2 group border border-gray-100">)(.*?<h3 class="text-xl font-bold mb-3 text-\[#242424\] group-hover:text-\[#ae8f73\] transition-colors">{s_name}</h3>.*?</div>\s*</div>)'
    
    match = re.search(search_pattern, content, re.DOTALL)
    if match:
        full_block = match.group(0)
        inner_content = match.group(2)
        
        # Change the outer div to an 'a' tag
        new_block = f'<a href="/{link}" class="block bg-white rounded-xl overflow-hidden shadow-[0_4px_20px_-4px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group border border-gray-100">{inner_content}</a>'
        content = content.replace(full_block, new_block)
    else:
        print(f"Failed to match {s_name}")

with open('index.html', 'w') as f:
    f.write(content)
print("Tiles fixed in index.html")
