import re

with open('tueren-fenster.html', 'r') as f:
    template = f.read()

# Replace Meta Data
template = template.replace(
    '<title>Türen & Fensterbau Landau – Holztüren vom Schreiner | Schreinerei Yacoub</title>',
    '<title>Innenausbau Landau – Holzverkleidung, Küche & Raumgestaltung | Schreinerei Yacoub</title>'
)
template = template.replace(
    '<meta name="description" content="Maßgefertigte Innentüren, Haustüren und Holzfenster vom Schreinermeister in Landau in der Pfalz. Funktional, langlebig und wunderschön.">',
    '<meta name="description" content="Innenausbau in Landau. Wandverkleidungen, Decken, Küchen nach Maß und Stauraumlösungen vom Schreinermeister. Stilvoll und langlebig.">'
)

# Hero Section
template = template.replace('Türen & Fenster in <br><span class="font-bold">Landau in der Pfalz</span>', 'Innenausbau in <br><span class="font-bold">Landau in der Pfalz</span>')
template = template.replace('Funktional. Langlebig. Schön. Maßgefertigte Türen und Fensterrahmen vom Schreinermeister für Ihr Zuhause.', 'Stilvoll. Maßgeschneidert. Langlebig. Verwandeln Sie Räume in perfekte Lebensräume.')
template = template.replace('tueren-fenster-2.jpeg', 'innenausbau-1.jpeg')

# Intro Section
template = template.replace('Türen & Fenster – Stil und <br><span class="font-bold">Funktion im Einklang</span>', 'Professioneller Innenausbau <br><span class="font-bold">vom Schreinermeister</span>')
template = template.replace('Türen und Fenster sind mehr als nur Bauelemente – sie verbinden Räume, schaffen Atmosphäre und prägen den Charakter eines Hauses. Bei der Schreinerei Yacoub aus Landau entstehen Holztüren und Fensterrahmen, die Ästhetik, Qualität und Funktion perfekt vereinen.', 'Ob gemütliche Wohnräume, moderne Büros oder stilvolle Küchen – mit dem Innenausbau der Schreinerei Yacoub verwandeln Sie Räume in Lebensräume. Wir planen und realisieren individuelle Holzverkleidungen, Einbauschränke, Wand- und Deckensysteme sowie Küchen nach Maß – immer präzise, funktional und perfekt abgestimmt auf Ihre Architektur.')
template = template.replace('Ob moderne Innentüren, maßgefertigte Haustüren oder Fensterrahmen aus Holz – wir fertigen und montieren individuell nach Ihren Vorstellungen, millimetergenau und in echter Schreinerqualität.', 'Als erfahrener Schreiner für Innenausbau in Landau kombinieren wir handwerkliches Können mit modernem Design. So entsteht eine Atmosphäre, die sowohl optisch begeistert als auch im Alltag überzeugt.')

# Portfolio Section - Item 1
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Zimmertüren</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Wand & Decke</div>')
template = template.replace('Holztüren für <br>Innenräume', 'Holzverkleidungen & <br>Akustiklösungen')
template = template.replace('Innentüren schaffen Struktur und Atmosphäre. Wir fertigen Zimmertüren aus Holz, Glas oder CPL, die perfekt zu Ihren Räumen passen – ob klassisch, modern oder rustikal. Sie wählen Oberfläche, Farbe, Griff und Form – wir sorgen für die passgenaue Umsetzung.', 'Holz schafft Wärme, Natürlichkeit und ein behagliches Wohngefühl. Wir verkleiden Wände und Decken mit edlen Hölzern, Paneelen oder modernen Akustiklösungen – ideal für Wohnräume, Büros oder repräsentative Eingangsbereiche.')
template = template.replace('Weißlack mit klarer Linienführung', 'Verbesserte Raumakustik')
template = template.replace('Echtholzfurnier mit Maserung', 'Edle Holzpaneele')
template = template.replace('Platzsparende Schiebetüren', 'Kombination mit Lichtsystemen')
template = template.replace('tueren-fenster-2.jpeg', 'innenausbau-2.jpeg')

# Portfolio Section - Item 2
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Eingangsbereich</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Stauraum</div>')
template = template.replace('Haustüren & <br>Wohnungseingang', 'Einbauschränke & <br>Garderoben')
template = template.replace('Die Haustür ist die Visitenkarte Ihres Hauses – sie soll einladen und schützen zugleich. Wir fertigen Haustüren aus massivem Holz oder Holz-Alu-Kombinationen mit Fokus auf Wärmedämmung, Langlebigkeit und Sicherheit.', 'Jeder Raum ist anders – und genau darauf reagieren wir. Unsere Einbauschränke nach Maß nutzen jede Nische optimal aus – ob im Flur, Schlafzimmer oder Dachgeschoss. Mit individuellen Fronten, Innenausstattung und Griffsystemen schaffen wir Stauraum mit Stil.')
template = template.replace('Einbruchhemmend nach DIN', 'Optimale Raumnutzung')
template = template.replace('Energiesparend & dicht', 'Individuelle Innenausstattung')
template = template.replace('Passend zu Ihrer Fassade', 'Perfekt für Nischen & Schrägen')
template = template.replace('tueren-fenster-3.jpeg', 'innenausbau-3.jpeg')

# Portfolio Section - Item 3
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Holzfenster</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Küchen</div>')
template = template.replace('Fensterrahmen & <br>Sonderelemente', 'Küchen nach <br>Maß')
template = template.replace('Fenster aus Holz bringen Natürlichkeit in jeden Raum. Wir fertigen Fensterrahmen nach Maß, sanieren alte Holzrahmen oder kombinieren Holz mit Aluminium für maximale Witterungsbeständigkeit. Auch Sonderlösungen setzen wir detailgenau um.', 'Die Küche ist das Herz des Hauses. Wir planen Küchen nach Maß, die perfekt zu Ihrer Raumgröße, Ihrem Stil und Ihren Kochgewohnheiten passen. Ob klassisch in Eiche, modern mit Lackfronten oder minimalistisch mit grifflosen Elementen – bei uns erhalten Sie Schreinerqualität statt Standardlösungen.')
template = template.replace('Denkmalgerechte Nachbauten', 'Individuelle Arbeitsplatten')
template = template.replace('Sprossenfenster', 'Massivholz & Lackfronten')
template = template.replace('Rundbogenförmige Fenster', 'Ergonomische Planung')
template = template.replace('tueren-fenster-4.jpeg', 'innenausbau-4.jpeg')

# Portfolio Section - Item 4
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Handwerkskunst</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Design</div>')
template = template.replace('Materialien & <br>Oberflächen', 'Decken- & <br>Raumgestaltung')
template = template.replace('Jede Tür und jeder Rahmen wird individuell gefertigt. Wir verwenden ausschließlich hochwertige Hölzer (Eiche, Buche, Ahorn, Nussbaum) und Beschläge namhafter Hersteller. Oberflächen werden je nach Stil geölt, lackiert oder furniert.', 'Unsere Deckenverkleidungen schaffen optische Struktur und können gleichzeitig Akustik und Beleuchtung verbessern. Wir integrieren Einbauleuchten, Lüftungselemente oder versteckte Kabelkanäle – alles harmonisch und funktional zugleich.')
template = template.replace('Eiche: robust & zeitlos', 'Versteckte Kabelkanäle')
template = template.replace('Buche & Ahorn: hell & modern', 'Integrierte Beleuchtung')
template = template.replace('Holz-Alu-Kombinationen', 'Optische Raumstruktur')
template = template.replace('tueren-und-fensterbau.jpeg', 'innenausbau-5.jpeg')

with open('innenausbau.html', 'w') as f:
    f.write(template)
print("innenausbau.html created")
