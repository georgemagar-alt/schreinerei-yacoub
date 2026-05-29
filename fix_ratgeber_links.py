import re

with open('ratgeber.html', 'r') as f:
    content = f.read()

# Replace links for articles
# 1. Parkett
content = re.sub(
    r'(<h3 class="[^"]*">Parkett pflegen und schleifen: Tipps vom Schreinermeister</h3>.*?<p class="[^"]*">.*?<a href=")("#)',
    r'\1/ratgeber-parkett-pflegen.html',
    content, flags=re.DOTALL
)

# 2. Dachschrägen
content = re.sub(
    r'(<h3 class="[^"]*">Einbauschrank für Dachschrägen: Jeden Zentimeter nutzen</h3>.*?<p class="[^"]*">.*?<a href=")("#)',
    r'\1/ratgeber-dachschraegen-schrank.html',
    content, flags=re.DOTALL
)

# 3. Massivholz vs Furnier
content = re.sub(
    r'(<h3 class="[^"]*">Massivholz oder Furnier\? Material für Ihre Möbel nach Maß</h3>.*?<p class="[^"]*">.*?<a href=")("#)',
    r'\1/ratgeber-massivholz-furnier.html',
    content, flags=re.DOTALL
)

# 4. Restauration
content = re.sub(
    r'(<h3 class="[^"]*">Alte Holzmöbel restaurieren lassen: Wann lohnt sich das\?</h3>.*?<p class="[^"]*">.*?<a href=")("#)',
    r'\1/ratgeber-moebel-restaurieren.html',
    content, flags=re.DOTALL
)

# 5. Holzfenster
content = re.sub(
    r'(<h3 class="[^"]*">Holzfenster sanieren oder tauschen\? Ratgeber für Altbauten</h3>.*?<p class="[^"]*">.*?<a href=")("#)',
    r'\1/ratgeber-holzfenster-sanieren.html',
    content, flags=re.DOTALL
)

with open('ratgeber.html', 'w') as f:
    f.write(content)
print("Updated ratgeber.html links")
