import re

cities = [
    {"slug": "landau", "display": "Landau i.d. Pfalz", "short": "Landau"},
    {"slug": "neustadt", "display": "Neustadt a.d.W.", "short": "Neustadt"},
    {"slug": "speyer", "display": "Speyer", "short": "Speyer"},
    {"slug": "karlsruhe", "display": "Karlsruhe", "short": "Karlsruhe"},
    {"slug": "weissenburg", "display": "Weißenburg", "short": "Weißenburg"},
    {"slug": "frankenthal", "display": "Frankenthal", "short": "Frankenthal"},
    {"slug": "bad-duerkheim", "display": "Bad Dürkheim", "short": "Bad Dürkheim"},
    {"slug": "pforzheim", "display": "Pforzheim", "short": "Pforzheim"},
    {"slug": "kaiserslautern", "display": "Kaiserslautern", "short": "Kaiserslautern"}
]

services = [
    {"file": "innenausbau.html", "name": "Innenausbau"},
    {"file": "massanfertigung.html", "name": "Maßanfertigung"},
    {"file": "moebelbau.html", "name": "Möbelbau"},
    {"file": "tueren-fenster.html", "name": "Türen & Fenster"},
    {"file": "restauration.html", "name": "Restauration"}
]

# 1. Generate Service Pages for each city
for s in services:
    with open(s["file"], 'r') as f:
        template = f.read()
    
    slug_prefix = s["file"].split('.html')[0]
    
    for c in cities:
        html = template
        
        # Titles and Meta
        html = re.sub(
            r'<title>.*?</title>',
            f'<title>{s["name"]} in {c["display"]} | Schreinerei Yacoub</title>',
            html
        )
        html = re.sub(
            r'<meta name="description" content="[^"]*">',
            f'<meta name="description" content="Ihr Experte für hochwertigen {s["name"]} in {c["display"]}. Schreinermeisterbetrieb Yacoub.">',
            html
        )
        
        # Replacements
        html = html.replace('Landau in der Pfalz', c['display'])
        html = html.replace('Schreinerei Yacoub in Landau', f'Schreinerei Yacoub für {c["short"]}')
        html = html.replace('Schreinermeisterbetrieb in Landau', f'Schreinermeisterbetrieb für {c["short"]}')
        html = html.replace('der Südpfalz', f'der Region {c["short"]}')
        
        filename = f"{slug_prefix}-{c['slug']}.html"
        with open(filename, 'w') as f:
            f.write(html)
        print(f"Generated {filename}")

# 2. Generate Hub Pages from index.html
with open('index.html', 'r') as f:
    hub_template = f.read()

for c in cities:
    html = hub_template
    
    # Meta / Title
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>Schreinerei Yacoub {c["display"]} – Möbelbau & Innenausbau</title>',
        html
    )
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="Ihr Schreinermeisterbetrieb für {c["display"]}. Wir bieten Maßanfertigungen, Innenausbau, Möbelbau und Bodenarbeiten.">',
        html
    )
    
    # Body Text Replacements
    html = html.replace('Landau in der Pfalz', c['display'])
    html = html.replace('Schreinerei Yacoub in Landau', f'Schreinerei Yacoub für {c["short"]}')
    html = html.replace('Schreinermeisterbetrieb in Landau', f'Schreinermeisterbetrieb für {c["short"]}')
    html = html.replace('der Südpfalz', f'der Region {c["short"]}')
    
    html = html.replace('Regional & zuverlässig – Landau, Rhein-Neckar & die Südpfalz.', f'Regional & zuverlässig – in {c["display"]} und der Region.')
    html = html.replace('Egal ob Landau in der Pfalz, Karlsruhe, Speyer, Neustadt, Mannheim oder Umland – wir sind hier zuhause.', f'Wir sind Ihr lokaler Ansprechpartner direkt in {c["display"]} und Umgebung.')
    
    # Update the service links on the hub page to point to local versions!
    html = html.replace('href="/bodenarbeiten.html"', f'href="/bodenarbeiten-{c["slug"]}.html"')
    html = html.replace('href="/innenausbau.html"', f'href="/innenausbau-{c["slug"]}.html"')
    html = html.replace('href="/moebelbau.html"', f'href="/moebelbau-{c["slug"]}.html"')
    html = html.replace('href="/tueren-fenster.html"', f'href="/tueren-fenster-{c["slug"]}.html"')
    html = html.replace('href="/massanfertigung.html"', f'href="/massanfertigung-{c["slug"]}.html"')
    html = html.replace('href="/restauration.html"', f'href="/restauration-{c["slug"]}.html"')
    
    filename = f"schreiner-{c['slug']}.html"
    with open(filename, 'w') as f:
        f.write(html)
    print(f"Generated Hub {filename}")
