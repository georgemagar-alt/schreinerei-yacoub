import re
import json

# Data for the 5 files
data = {
    'tueren-fenster': {
        'process_title': 'Der Weg zu neuen Türen & Fenstern',
        'process_subtitle': 'Unser Ablauf',
        'steps': [
            {'title': 'Beratung & Aufmaß', 'text': 'Wir beraten Sie vor Ort und nehmen exakt Maß für eine perfekte Passgenauigkeit.'},
            {'title': 'Auswahl & Angebot', 'text': 'Sie wählen Design und Material, wir erstellen ein transparentes, faires Angebot.'},
            {'title': 'Fertigung', 'text': 'In unserer Werkstatt werden Ihre Türen oder Fenster millimetergenau und hochwertig gefertigt.'},
            {'title': 'Montage', 'text': 'Wir bauen fachgerecht, sauber und nach aktuellen Energiestandards ein.'}
        ],
        'faq': [
            {'q': 'Bieten Sie auch einbruchhemmende Türen an?', 'a': 'Ja, wir fertigen Haustüren und Fenster mit modernster Sicherheitstechnik nach DIN-Norm.'},
            {'q': 'Können alte Holzfenster saniert werden?', 'a': 'In vielen Fällen ja. Wir prüfen den Zustand und arbeiten alte Rahmen auf oder rüsten Dichtungen nach.'},
            {'q': 'Wie lange dauert die Fertigung?', 'a': 'Je nach Modell und Umfang dauert die Maßanfertigung in der Regel 4 bis 8 Wochen.'},
            {'q': 'Bauen Sie auch Zimmertüren in Sondermaßen?', 'a': 'Ja, als Schreinerei fertigen wir jede Tür genau passend – auch für außergewöhnliche Maße oder Altbauten.'}
        ]
    },
    'moebelbau': {
        'process_title': 'So entsteht Ihr Möbelstück – Schritt für Schritt',
        'process_subtitle': 'Unser Ablauf',
        'steps': [
            {'title': 'Beratung & Ideenfindung', 'text': 'Gemeinsam besprechen wir Ihre Wünsche, Materialien und Stilrichtungen. Auf Wunsch bringen wir Muster und Beispiele mit.'},
            {'title': 'Aufmaß & Planung', 'text': 'Wir nehmen exakt Maß in Ihren Räumen und erstellen digitale Entwürfe – damit Sie sich das Ergebnis vorstellen können.'},
            {'title': 'Angebot & Freigabe', 'text': 'Sie erhalten ein transparentes, faires Angebot ohne versteckte Kosten.'},
            {'title': 'Fertigung & Montage', 'text': 'Mit Präzision entsteht Ihr Möbelstück. Wir liefern termingerecht und bauen alles fachmännisch bei Ihnen auf.'}
        ],
        'faq': [
            {'q': 'Können Sie Möbel nach einem Foto nachbauen?', 'a': 'Ja, wir können uns von Bildern inspirieren lassen und ein Möbelstück in ähnlichem Stil maßgenau für Sie anfertigen.'},
            {'q': 'Aus welchen Hölzern bauen Sie Möbel?', 'a': 'Wir verarbeiten alle gängigen Hölzer wie Eiche, Nussbaum, Buche oder Ahorn, aber auch besondere Edelhölzer – auf Wunsch FSC-zertifiziert.'},
            {'q': 'Ist Maßanfertigung immer teurer als Möbelhaus-Ware?', 'a': 'Ein Maßmöbel ist eine handwerkliche Einzelanfertigung, die für Langlebigkeit steht. Es ist eine Investition, die sich über Jahrzehnte auszahlt, anders als viele Industriemöbel.'},
            {'q': 'Bieten Sie auch Anpassungen bestehender Möbel an?', 'a': 'Ja, wir passen Möbel an neue Räumlichkeiten an, bauen sie um oder integrieren sie in neue Konzepte.'}
        ]
    },
    'innenausbau': {
        'process_title': 'Ablauf Ihres Innenausbau-Projekts',
        'process_subtitle': 'Unser Ablauf',
        'steps': [
            {'title': 'Beratung & Konzeptfindung', 'text': 'Wir klären Wünsche und Nutzung. Auf Wunsch besuchen wir Sie vor Ort, um Raumwirkung und Lichteinfall zu berücksichtigen.'},
            {'title': 'Aufmaß & Angebot', 'text': 'Wir nehmen präzise Maße und erstellen digitale Entwürfe sowie ein transparentes Angebot mit klarer Kostenaufstellung.'},
            {'title': 'Fertigung', 'text': 'Ihr Projekt wird mit moderner Technik und traditioneller Handwerkskunst in unserer Werkstatt umgesetzt.'},
            {'title': 'Montage & Übergabe', 'text': 'Wir montieren sauber und termintreu. Danach übergeben wir Ihnen Ihren fertig gestalteten Raum – einsatzbereit und makellos.'}
        ],
        'faq': [
            {'q': 'Welche Leistungen gehören zum Innenausbau?', 'a': 'Wir übernehmen Wand- und Deckenverkleidungen, Einbauschränke, Küchen, Garderoben, Holzdecken und Raumkonzepte nach Maß.'},
            {'q': 'Fertigen Sie auch Küchen individuell an?', 'a': 'Ja – jede Küche wird individuell geplant, gefertigt und montiert, inklusive Geräteintegration und Beleuchtung.'},
            {'q': 'Können Sie den Innenausbau im Altbau übernehmen?', 'a': 'Selbstverständlich. Wir sind spezialisiert auf Altbauprojekte und passen neue Elemente präzise an bestehende Strukturen an.'},
            {'q': 'Arbeiten Sie mit anderen Gewerken zusammen?', 'a': 'Ja, wir koordinieren bei Bedarf Maler, Elektriker oder Bodenleger – für ein rundum stimmiges Ergebnis.'},
            {'q': 'Wie lange dauert ein Innenausbau-Projekt?', 'a': 'Je nach Umfang etwa 3–8 Wochen ab Freigabe der Planung.'}
        ]
    },
    'restauration': {
        'process_title': 'Vorgehensweise bei Möbelrestauration',
        'process_subtitle': 'Unser Ablauf',
        'steps': [
            {'title': 'Begutachtung & Beratung', 'text': 'Wir begutachten das Möbelstück in unserer Werkstatt oder bei Ihnen zu Hause. Wir klären Zustand, Alter und Restaurationsziel.'},
            {'title': 'Kostenvoranschlag', 'text': 'Sie erhalten ein transparentes Angebot – abgestimmt auf Aufwand und gewünschtes Ergebnis.'},
            {'title': 'Restauration', 'text': 'Mit viel Feingefühl, handwerklichem Wissen und passenden Materialien arbeiten wir Ihr Möbelstück fachgerecht auf.'},
            {'title': 'Übergabe', 'text': 'Sie erhalten Ihr Schmuckstück zurück – funktionsfähig, gepflegt und bereit für die nächsten Jahrzehnte.'}
        ],
        'faq': [
            {'q': 'Lohnt sich die Restauration alter Möbel?', 'a': 'In den meisten Fällen ja. Antike oder familiäre Erbstücke haben oft eine viel höhere Materialqualität als moderne Möbel und einen unersetzbaren ideellen Wert.'},
            {'q': 'Holen Sie die Möbel ab?', 'a': 'Ja, wir bieten im Raum Landau und der Südpfalz einen Hol- und Bringservice für Ihre Restaurationsstücke an.'},
            {'q': 'Können Holzwurmschäden repariert werden?', 'a': 'Ja. Nach einer erfolgreichen Schädlingsbekämpfung können wir Löcher, Fraßgänge und Strukturverluste oft so ausbessern, dass sie kaum noch sichtbar sind.'},
            {'q': 'Ist eine Restauration immer auf Hochglanz?', 'a': 'Nein, wir können auch eine gewollte Patina (Shabby Chic) erhalten oder alte Möbel bewusst matt aufarbeiten. Sie entscheiden über den Stil.'}
        ]
    },
    'massanfertigung': {
        'process_title': 'Unser Prozess – von der Idee zum Unikat',
        'process_subtitle': 'Unser Ablauf',
        'steps': [
            {'title': 'Beratung & Inspiration', 'text': 'Wir nehmen uns Zeit, Ihre Vorstellungen kennenzulernen. Dabei geht es um Funktion, Design, Farben und Materialien.'},
            {'title': 'Aufmaß & Entwurf', 'text': 'Wir messen präzise und erstellen 3D-Entwürfe – damit Sie Ihr Möbel schon vorab sehen können.'},
            {'title': 'Material- & Angebot', 'text': 'Wir legen die exakten Materialien fest und Sie erhalten ein verbindliches, transparentes Angebot.'},
            {'title': 'Fertigung & Montage', 'text': 'Nach sorgfältiger Herstellung in unserer Schreinerei montieren wir Ihr neues Unikat bei Ihnen vor Ort.'}
        ],
        'faq': [
            {'q': 'Was kostet eine Maßanfertigung?', 'a': 'Der Preis hängt von Größe, Material und Aufwand ab. Nach einem ersten Gespräch können wir Ihnen meist schon eine grobe Einschätzung geben.'},
            {'q': 'Kommen Sie auch für kleine Projekte?', 'a': 'Absolut. Ob einzelnes Wandregal, Bad-Spiegelschrank oder eine kleine Nischenverkleidung – wir fertigen mit der gleichen Sorgfalt.'},
            {'q': 'Welche Materialien bieten Sie an?', 'a': 'Wir verarbeiten alle Holzarten (Massivholz und Furnier), Plattenwerkstoffe, Lackoberflächen und kombinieren gerne mit Glas, Metall oder Linoleum.'},
            {'q': 'Können Sie Möbelstücke farblich an meinen Bestand anpassen?', 'a': 'Ja, durch spezielle Beizen, Öle oder farbgenaue Lackierungen können wir neue Möbel an bestehende Einrichtungen anpassen.'}
        ]
    }
}

template_process = """    <!-- Process Section -->
    <section class="py-24 bg-[#1a1a1a] text-white">
        <div class="container mx-auto px-4 max-w-7xl">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-8 border-b border-white/10 pb-8">
                <div class="max-w-2xl">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-8 h-[1px] bg-[#ae8f73]"></div>
                        <span class="text-[#ae8f73] uppercase tracking-widest text-xs font-bold">{process_title}</span>
                    </div>
                    <h2 class="text-3xl md:text-5xl font-light tracking-tight">{process_subtitle}</h2>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
{steps_html}
            </div>
        </div>
    </section>"""

template_step = """                <div class="border-t border-white/10 pt-8">
                    <div class="text-4xl font-light text-[#ae8f73] mb-6">0{idx}.</div>
                    <h4 class="text-xl font-bold mb-4">{title}</h4>
                    <p class="text-gray-400 text-sm leading-relaxed">{text}</p>
                </div>"""

template_faq = """

    <!-- FAQ Section -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-4 max-w-3xl">
            <div class="text-center mb-16">
                <h2 class="text-sm font-bold text-[#ae8f73] uppercase tracking-[0.2em] mb-4">FAQ</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-[#1a1a1a] tracking-tight">Häufig gestellte Fragen</h3>
            </div>

            <div class="space-y-4">
{faq_items_html}
            </div>
        </div>
    </section>
"""

template_faq_item = """                <!-- FAQ Item {idx} -->
                <details class="group border border-gray-200 rounded-xl bg-white [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between gap-1.5 p-6 text-[#1a1a1a]">
                        <h4 class="font-bold text-lg">{q}</h4>
                        <span class="relative size-5 shrink-0">
                            <svg class="absolute inset-0 size-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <svg class="absolute inset-0 size-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                        </span>
                    </summary>
                    <div class="px-6 pb-6 text-gray-600 leading-relaxed">
                        {a}
                    </div>
                </details>"""

for page_id, info in data.items():
    filename = page_id + '.html'
    
    # Generate Process HTML
    steps_html = '\n'.join([template_step.format(idx=i+1, title=step['title'], text=step['text']) for i, step in enumerate(info['steps'])])
    process_html = template_process.format(
        process_title=info['process_title'], 
        process_subtitle=info['process_subtitle'], 
        steps_html=steps_html
    )
    
    # Generate FAQ HTML
    faq_items_html = '\n'.join([template_faq_item.format(idx=i+1, q=faq['q'], a=faq['a']) for i, faq in enumerate(info['faq'])])
    faq_html = template_faq.format(faq_items_html=faq_items_html)
    
    replacement_block = process_html + faq_html
    
    with open(filename, 'r') as f:
        content = f.read()
        
    # Replace block between <!-- Process Section --> and <!-- Contact & Form Section -->
    pattern = re.compile(r'<!-- Process Section -->.*?<!-- Contact & Form Section -->', re.DOTALL)
    new_content = pattern.sub(replacement_block + '\n    <!-- Contact & Form Section -->', content)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Updated {filename}")

