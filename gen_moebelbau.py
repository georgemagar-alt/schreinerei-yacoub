import re

with open('tueren-fenster.html', 'r') as f:
    template = f.read()

# Replace Meta Data
template = template.replace(
    '<title>Türen & Fensterbau Landau – Holztüren vom Schreiner | Schreinerei Yacoub</title>',
    '<title>Möbelbau Landau – Möbel nach Maß & Holzmanufaktur | Schreinerei Yacoub</title>'
)
template = template.replace(
    '<meta name="description" content="Maßgefertigte Innentüren, Haustüren und Holzfenster vom Schreinermeister in Landau in der Pfalz. Funktional, langlebig und wunderschön.">',
    '<meta name="description" content="Möbel nach Maß vom Schreinermeister in Landau. Einbauschränke, Regale, Tische und mehr – individuell für Sie gefertigt.">'
)

# Hero Section
template = template.replace('Türen & Fenster in <br><span class="font-bold">Landau in der Pfalz</span>', 'Möbelbau in <br><span class="font-bold">Landau in der Pfalz</span>')
template = template.replace('Funktional. Langlebig. Schön. Maßgefertigte Türen und Fensterrahmen vom Schreinermeister für Ihr Zuhause.', 'Schnell. Zeitlos. Effizient. Maßgefertigte Möbel und Holzmanufaktur vom Schreinermeister.')
template = template.replace('tueren-fenster-2.jpeg', 'moebelbau-1.jpeg')

# Intro Section
template = template.replace('Türen & Fenster – Stil und <br><span class="font-bold">Funktion im Einklang</span>', 'Professioneller Möbelbau in <br><span class="font-bold">Landau & Umgebung</span>')
template = template.replace('Türen und Fenster sind mehr als nur Bauelemente – sie verbinden Räume, schaffen Atmosphäre und prägen den Charakter eines Hauses. Bei der Schreinerei Yacoub aus Landau entstehen Holztüren und Fensterrahmen, die Ästhetik, Qualität und Funktion perfekt vereinen.', 'In unserer Schreinerei Yacoub in Landau entstehen Möbel, die mehr sind als reine Einrichtungsstücke. Sie erzählen Geschichten – aus natürlichem Holz, echter Handarbeit und Ihrer persönlichen Vorstellung.')
template = template.replace('Ob moderne Innentüren, maßgefertigte Haustüren oder Fensterrahmen aus Holz – wir fertigen und montieren individuell nach Ihren Vorstellungen, millimetergenau und in echter Schreinerqualität.', 'Wir fertigen Möbel, die genau zu Ihrem Stil, Ihren Räumen und Ihrem Alltag passen. Als erfahrene Möbeltischlerei und Holzmanufaktur verbinden wir traditionelle Schreinerkunst mit modernen Fertigungstechniken. So entstehen zeitlose Möbel nach Maß, die nicht nur ästhetisch, sondern auch langlebig und praktisch sind.')

# Portfolio Section - Item 1
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Zimmertüren</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Schränke & Einbau</div>')
template = template.replace('Holztüren für <br>Innenräume', 'Schränke & <br>Einbaumöbel')
template = template.replace('Innentüren schaffen Struktur und Atmosphäre. Wir fertigen Zimmertüren aus Holz, Glas oder CPL, die perfekt zu Ihren Räumen passen – ob klassisch, modern oder rustikal. Sie wählen Oberfläche, Farbe, Griff und Form – wir sorgen für die passgenaue Umsetzung.', 'Ein Einbauschrank nach Maß nutzt jeden Zentimeter optimal aus – ob in Dachschrägen, Nischen oder Fluren. Wir planen Stauraum, der sich nahtlos in Ihre Räume einfügt und optisch überzeugt. Von der minimalistischen Front bis zur klassischen Echtholzoptik – Sie wählen Stil, Farbe und Beschläge.')
template = template.replace('Weißlack mit klarer Linienführung', 'Passgenau für Dachschrägen')
template = template.replace('Echtholzfurnier mit Maserung', 'Minimalistische Fronten')
template = template.replace('Platzsparende Schiebetüren', 'Klassische Echtholzoptik')
template = template.replace('tueren-fenster-2.jpeg', 'moebelbau-2.jpeg')

# Portfolio Section - Item 2
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Eingangsbereich</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Aufbewahrung</div>')
template = template.replace('Haustüren & <br>Wohnungseingang', 'Regale & <br>Aufbewahrung')
template = template.replace('Die Haustür ist die Visitenkarte Ihres Hauses – sie soll einladen und schützen zugleich. Wir fertigen Haustüren aus massivem Holz oder Holz-Alu-Kombinationen mit Fokus auf Wärmedämmung, Langlebigkeit und Sicherheit.', 'Unsere Regalsysteme nach Maß schaffen Ordnung mit Stil. Ob für Bücher, Sammlungen oder Dekoration – jedes Regal wird millimetergenau gefertigt. Auf Wunsch integrieren wir auch Lichtleisten, Schiebetüren oder Kombinationen aus Holz und Metall.')
template = template.replace('Einbruchhemmend nach DIN', 'Bücherregale & Bibliotheken')
template = template.replace('Energiesparend & dicht', 'Integrierte Lichtleisten')
template = template.replace('Passend zu Ihrer Fassade', 'Kombinationen mit Metall')
template = template.replace('tueren-fenster-3.jpeg', 'moebelbau-3.jpeg')

# Portfolio Section - Item 3
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Holzfenster</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Essbereich</div>')
template = template.replace('Fensterrahmen & <br>Sonderelemente', 'Tische & <br>Sitzmöbel')
template = template.replace('Fenster aus Holz bringen Natürlichkeit in jeden Raum. Wir fertigen Fensterrahmen nach Maß, sanieren alte Holzrahmen oder kombinieren Holz mit Aluminium für maximale Witterungsbeständigkeit. Auch Sonderlösungen setzen wir detailgenau um.', 'Ein Tisch ist ein Ort der Begegnung. Wir fertigen Esstische, Couchtische oder Sitzbänke aus massiven Hölzern wie Eiche, Nussbaum oder Buche. Mit einer natürlichen Oberfläche geölt oder lackiert, robust für den Alltag und edel im Design.')
template = template.replace('Denkmalgerechte Nachbauten', 'Massive Esstische')
template = template.replace('Sprossenfenster', 'Couchtische & Sitzbänke')
template = template.replace('Rundbogenförmige Fenster', 'Natürlich geölt oder lackiert')
template = template.replace('tueren-fenster-4.jpeg', 'moebelbau-4.jpeg')

# Portfolio Section - Item 4
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Handwerkskunst</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Schlafraum</div>')
template = template.replace('Materialien & <br>Oberflächen', 'Betten & <br>Schlafzimmer')
template = template.replace('Jede Tür und jeder Rahmen wird individuell gefertigt. Wir verwenden ausschließlich hochwertige Hölzer (Eiche, Buche, Ahorn, Nussbaum) und Beschläge namhafter Hersteller. Oberflächen werden je nach Stil geölt, lackiert oder furniert.', 'Ein gutes Bett ist mehr als ein Möbelstück – es ist ein Ort der Ruhe. Wir bauen Betten und Nachtmöbel nach Maß, die durch natürliche Materialien und präzise Verarbeitung überzeugen. Harmonie, Funktion und Design bilden dabei eine Einheit.')
template = template.replace('Eiche: robust & zeitlos', 'Maßgefertigte Betten')
template = template.replace('Buche & Ahorn: hell & modern', 'Passende Nachtmöbel')
template = template.replace('Holz-Alu-Kombinationen', 'Ökologisch & nachhaltig')
template = template.replace('tueren-und-fensterbau.jpeg', 'moebelbau-5.jpeg')

with open('moebelbau.html', 'w') as f:
    f.write(template)
print("moebelbau.html created")
