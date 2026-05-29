import re

with open('tueren-fenster.html', 'r') as f:
    template = f.read()

# Replace Meta Data
template = template.replace(
    '<title>Türen & Fensterbau Landau – Holztüren vom Schreiner | Schreinerei Yacoub</title>',
    '<title>Möbelrestauration Landau – Aufarbeitung alter Holzmöbel | Schreinerei Yacoub</title>'
)
template = template.replace(
    '<meta name="description" content="Maßgefertigte Innentüren, Haustüren und Holzfenster vom Schreinermeister in Landau in der Pfalz. Funktional, langlebig und wunderschön.">',
    '<meta name="description" content="Professionelle Möbelrestauration in Landau. Wir reparieren, pflegen und arbeiten Ihre alten Holzmöbel mit viel Liebe zum Detail auf.">'
)

# Hero Section
template = template.replace('Türen & Fenster in <br><span class="font-bold">Landau in der Pfalz</span>', 'Möbelrestauration in <br><span class="font-bold">Landau in der Pfalz</span>')
template = template.replace('Funktional. Langlebig. Schön. Maßgefertigte Türen und Fensterrahmen vom Schreinermeister für Ihr Zuhause.', 'Alte Möbel, neuer Glanz – mit Liebe zum Detail. Professionelle Aufarbeitung alter Holzmöbel.')
template = template.replace('tueren-fenster-2.jpeg', 'restauration-1.jpeg')

# Intro Section
template = template.replace('Türen & Fenster – Stil und <br><span class="font-bold">Funktion im Einklang</span>', 'Professionelle Restauration <br><span class="font-bold">vom Schreinermeister</span>')
template = template.replace('Türen und Fenster sind mehr als nur Bauelemente – sie verbinden Räume, schaffen Atmosphäre und prägen den Charakter eines Hauses. Bei der Schreinerei Yacoub aus Landau entstehen Holztüren und Fensterrahmen, die Ästhetik, Qualität und Funktion perfekt vereinen.', 'Jedes alte Möbelstück erzählt eine Geschichte – von Handwerkskunst, Familienerinnerungen oder besonderen Momenten. Mit der Schreinerei Yacoub in Landau bewahren Sie diesen Wert und bringen Ihre Möbel wieder zum Strahlen. Ob antike Kommode, historischer Schrank, Stuhl oder Tisch – wir restaurieren, reparieren und pflegen Ihre Stücke mit Erfahrung, Gefühl und höchster Präzision.')
template = template.replace('Ob moderne Innentüren, maßgefertigte Haustüren oder Fensterrahmen aus Holz – wir fertigen und montieren individuell nach Ihren Vorstellungen, millimetergenau und in echter Schreinerqualität.', 'In unserer Werkstatt vereinen wir traditionelle Restaurierungstechniken mit moderner Oberflächenbearbeitung. So bleibt der ursprüngliche Charakter erhalten, während Funktion und Schönheit zurückkehren.')

# Portfolio Section - Item 1
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Zimmertüren</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Aufarbeitung</div>')
template = template.replace('Holztüren für <br>Innenräume', 'Aufarbeitung & <br>Reparatur')
template = template.replace('Innentüren schaffen Struktur und Atmosphäre. Wir fertigen Zimmertüren aus Holz, Glas oder CPL, die perfekt zu Ihren Räumen passen – ob klassisch, modern oder rustikal. Sie wählen Oberfläche, Farbe, Griff und Form – wir sorgen für die passgenaue Umsetzung.', 'Wir reparieren beschädigte Teile, ersetzen defekte Beschläge und bessern Risse oder Abplatzungen aus. Dabei achten wir darauf, Originalteile zu erhalten, wann immer möglich. Fehlende Elemente fertigen wir originalgetreu nach.')
template = template.replace('Weißlack mit klarer Linienführung', 'Originalteile erhalten')
template = template.replace('Echtholzfurnier mit Maserung', 'Beschläge ersetzen')
template = template.replace('Platzsparende Schiebetüren', 'Fehlende Elemente nachfertigen')
template = template.replace('tueren-fenster-2.jpeg', 'restauration-2.jpeg')

# Portfolio Section - Item 2
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Eingangsbereich</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Oberflächen</div>')
template = template.replace('Haustüren & <br>Wohnungseingang', 'Oberflächen- <br>behandlung')
template = template.replace('Die Haustür ist die Visitenkarte Ihres Hauses – sie soll einladen und schützen zugleich. Wir fertigen Haustüren aus massivem Holz oder Holz-Alu-Kombinationen mit Fokus auf Wärmedämmung, Langlebigkeit und Sicherheit.', 'Je nach Zustand werden alte Lacke, Polituren oder Öle entfernt und die Oberfläche neu aufgebaut. Ob Schellack, Öl, Wachs oder Lack – wir wählen die passende Methode für jedes Holz und jede Epoche.')
template = template.replace('Einbruchhemmend nach DIN', 'Alte Lacke & Polituren entfernen')
template = template.replace('Energiesparend & dicht', 'Schellack & Wachs')
template = template.replace('Passend zu Ihrer Fassade', 'Passend zur Epoche')
template = template.replace('tueren-fenster-3.jpeg', 'restauration-3.jpeg')

# Portfolio Section - Item 3
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Holzfenster</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Ergänzung</div>')
template = template.replace('Fensterrahmen & <br>Sonderelemente', 'Ergänzung & <br>Anpassung')
template = template.replace('Fenster aus Holz bringen Natürlichkeit in jeden Raum. Wir fertigen Fensterrahmen nach Maß, sanieren alte Holzrahmen oder kombinieren Holz mit Aluminium für maximale Witterungsbeständigkeit. Auch Sonderlösungen setzen wir detailgenau um.', 'Fehlende Leisten, Furniere oder Intarsien rekonstruieren wir in Handarbeit. Wenn nötig, passen wir alte Möbel an moderne Nutzungsanforderungen an – etwa durch neue Schubladenauszüge, Scharniere oder Innenaufteilungen.')
template = template.replace('Denkmalgerechte Nachbauten', 'Rekonstruktion von Furnieren')
template = template.replace('Sprossenfenster', 'Intarsien in Handarbeit')
template = template.replace('Rundbogenförmige Fenster', 'Anpassung an moderne Nutzung')
template = template.replace('tueren-fenster-4.jpeg', 'restauration-4.jpeg')

# Portfolio Section - Item 4
template = template.replace('<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Handwerkskunst</div>', '<div class="text-[#ae8f73] font-bold tracking-widest text-sm mb-6 uppercase">Holzpflege</div>')
template = template.replace('Materialien & <br>Oberflächen', 'Reinigung & <br>Holzpflege')
template = template.replace('Jede Tür und jeder Rahmen wird individuell gefertigt. Wir verwenden ausschließlich hochwertige Hölzer (Eiche, Buche, Ahorn, Nussbaum) und Beschläge namhafter Hersteller. Oberflächen werden je nach Stil geölt, lackiert oder furniert.', 'Vor jeder Restauration steht eine gründliche Reinigung. Wir entfernen Staub, Schmutz, alte Polituren oder Nikotinbeläge – damit die natürliche Maserung und der ursprüngliche Farbton wieder sichtbar werden.')
template = template.replace('Eiche: robust & zeitlos', 'Schonende Tiefenreinigung')
template = template.replace('Buche & Ahorn: hell & modern', 'Entfernung alter Beläge')
template = template.replace('Holz-Alu-Kombinationen', 'Sichtbare natürliche Maserung')
template = template.replace('tueren-und-fensterbau.jpeg', 'restauration-5.jpeg')

with open('restauration.html', 'w') as f:
    f.write(template)
print("restauration.html created")
