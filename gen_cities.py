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

with open('bodenarbeiten.html', 'r') as f:
    template = f.read()

for c in cities:
    html = template
    
    # 1. Meta / Title
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>Bodenarbeiten in {c["display"]} | Schreinerei Yacoub</title>',
        html
    )
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="Ihr Experte für professionelle Bodenarbeiten in {c["display"]}. Parkett, Vinyl, Dielen verlegen lassen vom Schreinermeister.">',
        html
    )
    
    # 2. Text Replacements
    # Since 'Landau in der Pfalz' contains 'Landau', replace the longer one first
    html = html.replace('Landau in der Pfalz', c['display'])
    
    # Only replace 'Landau' in text contexts (not in href="/...landau...") if possible, but we don't have those links yet
    html = html.replace('Schreinerei Yacoub in Landau', f'Schreinerei Yacoub für {c["short"]}')
    html = html.replace('Schreinermeisterbetrieb in Landau', f'Schreinermeisterbetrieb für {c["short"]}')
    html = html.replace('der Südpfalz', f'der Region {c["short"]}')
    
    # Write file
    filename = f"bodenarbeiten-{c['slug']}.html"
    with open(filename, 'w') as f:
        f.write(html)
    print(f"Generated {filename}")

