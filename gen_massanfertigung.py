import re

with open('tueren-fenster.html', 'r') as f:
    template = f.read()

# Replace Meta Data
template = template.replace(
    '<title>Türen & Fensterbau Landau – Holztüren vom Schreiner | Schreinerei Yacoub</title>',
    '<title>Maßanfertigungen Landau – Möbel nach Maß & individuelle Lösungen | Schreinerei Yacoub</title>'
)
template = template.replace(
    '<meta name="description" content="Maßgefertigte Innentüren, Haustüren und Holzfenster vom Schreinermeister in Landau in der Pfalz. Funktional, langlebig und wunderschön.">',
    '<meta name="description" content="Maßanfertigungen in Landau in der Pfalz. Individuelle Schreinerlösungen, Einbauschränke und besondere Möbelstücke nach Maß.">'
)

# Hero Section
template = template.replace('Türen & Fenster in <br><span class="font-bold">Landau in der Pfalz</span>', 'Maßanfertigungen in <br><span class="font-bold">Landau in der Pfalz</span>')
template = template.replace('Funktional. Langlebig. Schön. Maßgefertigte Türen und Fensterrahmen vom Schreinermeister für Ihr Zuhause.', 'Ihre Ideen, unser Handwerk. Individuelle Schreinerlösungen – passgenau, persönlich & einzigartig.')
template = template.replace('tueren-fenster-2.jpeg', 'massanfertigung-1.jpeg')

# Intro Section
template = template.replace('Türen & Fenster – Stil und <br><span class="font-bold">Funktion im Einklang</span>', 'Ihre Ideen, <br><span class="font-bold">unser Handwerk</span>')
template = template.replace('Türen und Fenster sind mehr als nur Bauelemente – sie verbinden Räume, schaffen Atmosphäre und prägen den Charakter eines Hauses. Bei der Schreinerei Yacoub aus Landau entstehen Holztüren und Fensterrahmen, die Ästhetik, Qualität und Funktion perfekt vereinen.', 'Manche Räume brauchen mehr als Möbel von der Stange – sie brauchen Ideen, die perfekt passen. In unserer Schreinerei Yacoub in Landau entstehen individuelle Maßanfertigungen, die sich exakt nach Ihren Vorstellungen, Räumen und Bedürfnissen richten. Ob maßgefertigter Einbauschrank, Garderobe, Sideboard oder Möbelunikat – wir verwandeln Ihre Ideen in langlebige Lösungen aus Holz.')
template = template.replace('Ob moderne Innentüren, maßgefertigte Haustüren oder Fensterrahmen aus Holz – wir fertigen und montieren individuell nach Ihren Vorstellungen, millimetergenau und in echter Schreinerqualität.', 'Hier trifft traditionelles Handwerk auf moderne Planung & Designkompetenz – damit aus Ihrem Wunsch ein Unikat wird, das exakt zu Ihnen passt.')

# Portfolio Section - Item 1
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Zimmertüren</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Stauraum</div>')
template = template.replace('Holztüren für <br>Innenräume', 'Einbauschränke & <br>Stauraumlösungen')
template = template.replace('Innentüren schaffen Struktur und Atmosphäre. Wir fertigen Zimmertüren aus Holz, Glas oder CPL, die perfekt zu Ihren Räumen passen – ob klassisch, modern oder rustikal. Sie wählen Oberfläche, Farbe, Griff und Form – wir sorgen für die passgenaue Umsetzung.', 'Nutzen Sie jeden Zentimeter Ihrer Räume perfekt aus. Unsere Einbauschränke nach Maß fügen sich millimetergenau in Nischen, Dachschrägen oder Flure ein – mit Innenausstattung, Beleuchtung und Design nach Wunsch. Ob klassisch in Weiß, mit Echtholzfronten oder in trendigem Mattlack – wir gestalten Stauraum mit Stil.')
template = template.replace('Weißlack mit klarer Linienführung', 'Millimetergenaue Anpassung')
template = template.replace('Echtholzfurnier mit Maserung', 'Individuelle Innenausstattung')
template = template.replace('Platzsparende Schiebetüren', 'Echtholz- oder Mattlackfronten')
template = template.replace('tueren-fenster-2.jpeg', 'massanfertigung-2.jpeg')

# Portfolio Section - Item 2
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Eingangsbereich</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Möbel</div>')
template = template.replace('Haustüren & <br>Wohnungseingang', 'Sideboards, Kommoden <br>& Regale')
template = template.replace('Die Haustür ist die Visitenkarte Ihres Hauses – sie soll einladen und schützen zugleich. Wir fertigen Haustüren aus massivem Holz oder Holz-Alu-Kombinationen mit Fokus auf Wärmedämmung, Langlebigkeit und Sicherheit.', 'Wir fertigen Sideboards und Regale, die optisch und funktional überzeugen. Jede Kombination aus Holz, Glas oder Metall wird individuell geplant – als eleganter Blickfang oder praktische Aufbewahrungslösung.')
template = template.replace('Einbruchhemmend nach DIN', 'Holz, Glas oder Metall')
template = template.replace('Energiesparend & dicht', 'Elegante Blickfänge')
template = template.replace('Passend zu Ihrer Fassade', 'Individuell geplant')
template = template.replace('tueren-fenster-3.jpeg', 'massanfertigung-3.jpeg')

# Portfolio Section - Item 3
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Holzfenster</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Funktionalität</div>')
template = template.replace('Fensterrahmen & <br>Sonderelemente', 'Arbeits-, Bad- & <br>Küchenmöbel')
template = template.replace('Fenster aus Holz bringen Natürlichkeit in jeden Raum. Wir fertigen Fensterrahmen nach Maß, sanieren alte Holzrahmen oder kombinieren Holz mit Aluminium für maximale Witterungsbeständigkeit. Auch Sonderlösungen setzen wir detailgenau um.', 'Auch funktionale Möbel können schön sein. Wir entwerfen Badmöbel, Waschtischunterschränke oder Küchenmodule, die perfekt zu Ihren Geräten und Ihrem Stil passen – robust, ästhetisch und pflegeleicht.')
template = template.replace('Denkmalgerechte Nachbauten', 'Passgenaue Badmöbel')
template = template.replace('Sprossenfenster', 'Waschtischunterschränke')
template = template.replace('Rundbogenförmige Fenster', 'Ästhetisch & pflegeleicht')
template = template.replace('tueren-fenster-4.jpeg', 'massanfertigung-4.jpeg')

# Portfolio Section - Item 4
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Handwerkskunst</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Materialien</div>')
template = template.replace('Materialien & <br>Oberflächen', 'Materialien & <br>Designmöglichkeiten')
template = template.replace('Jede Tür und jeder Rahmen wird individuell gefertigt. Wir verwenden ausschließlich hochwertige Hölzer (Eiche, Buche, Ahorn, Nussbaum) und Beschläge namhafter Hersteller. Oberflächen werden je nach Stil geölt, lackiert oder furniert.', 'Unsere Maßanfertigungen entstehen aus hochwertigen Materialien: Massivholz für Robustheit und Wärme, Lack- und Dekoroberflächen für Individualität in Farbe und Struktur. Wir kombinieren Materialien harmonisch und achten auf Haptik, Lichtwirkung & Raumgefühl. So entstehen Möbel, die in Form und Funktion überzeugen.')
template = template.replace('Eiche: robust & zeitlos', 'Massivholz: warm & langlebig')
template = template.replace('Buche & Ahorn: hell & modern', 'Lack & Dekor: individuell')
template = template.replace('Holz-Alu-Kombinationen', 'Haptik & Lichtwirkung')
template = template.replace('tueren-und-fensterbau.jpeg', 'massanfertigung-5.jpeg')

with open('massanfertigung.html', 'w') as f:
    f.write(template)
print("massanfertigung.html created")
