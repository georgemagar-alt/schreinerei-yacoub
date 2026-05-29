import re

with open('ratgeber.html', 'r') as f:
    template = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', template, re.DOTALL)
head = head_match.group(1) if head_match else ''

# Extract header
header_match = re.search(r'(<!-- Header / Nav -->.*?</header>)', template, re.DOTALL)
header = header_match.group(1) if header_match else ''

# Extract footer
footer_match = re.search(r'(<!-- Contact & Form Section -->.*</body>\s*</html>)', template, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

articles_data = [
    {
        'id': 'ratgeber-parkett-pflegen',
        'title': 'Parkett pflegen und schleifen: Tipps vom Schreinermeister',
        'category': 'Bodenarbeiten',
        'image': '/assets/images/bodenarbeiten.jpeg',
        'content': """
            <p class="text-xl text-gray-600 leading-relaxed mb-8 font-light">Ein massiver Holzboden ist eine Investition fürs Leben. Doch um seine natürliche Schönheit und Widerstandsfähigkeit über Jahrzehnte zu erhalten, bedarf es der richtigen Pflege. Als erfahrene Schreinerei in Landau teilen wir unsere besten Tipps zur Pflege von geöltem und lackiertem Parkett.</p>
            
            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Geöltes vs. Lackiertes Parkett: Was ist der Unterschied?</h2>
            <p class="mb-6">Die Wahl der Oberflächenbehandlung hat einen enormen Einfluss darauf, wie ein Holzboden gereinigt und gepflegt werden muss.</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li><strong>Geöltes Parkett:</strong> Das Öl dringt tief in die Holzporen ein und schützt von innen. Die Holzmaserung bleibt spürbar, der Boden kann atmen. Kratzer lassen sich oft partiell ausbessern. Allerdings erfordert er regelmäßiges Nachölen.</li>
                <li><strong>Lackiertes Parkett:</strong> Der Lack bildet eine geschlossene Schutzschicht auf dem Holz. Er ist besonders pflegeleicht und wasserabweisend. Wenn jedoch tiefe Kratzer entstehen, muss oft der gesamte Raum abgeschliffen werden.</li>
            </ul>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Die richtige Unterhaltsreinigung</h2>
            <p class="mb-6">Weniger ist beim Holzboden oft mehr. Für die alltägliche Reinigung reicht meist das Fegen oder Staubsaugen (mit spezieller Parkettbürste). Beim Wischen gilt stets der Grundsatz: <strong>Nur nebelfeucht wischen!</strong></p>
            <p class="mb-8">Stehendes Wasser ist der größte Feind jedes Holzbodens, da es in die Fugen eindringen und das Holz zum Aufquellen bringen kann. Verwenden Sie zudem niemals aggressive Allzweckreiniger oder Mikrofasertücher, da diese mikrofeine Kratzer im Lack verursachen oder dem geölten Holz die Schutzschicht entziehen.</p>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Wann muss der Holzboden abgeschliffen werden?</h2>
            <p class="mb-6">Ein massiver Parkettboden kann im Laufe seines Lebens mehrfach abgeschliffen werden – das ist sein größter Vorteil gegenüber Laminat oder Vinyl. Ein Abschliff durch den Fachmann ist empfehlenswert, wenn:</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li>Tiefe Kratzer oder Dellen das Gesamtbild stören</li>
                <li>Die Laufstraßen stark abgenutzt, verfärbt oder stumpf sind</li>
                <li>Hartnäckige Wasserflecken (z.B. durch Blumentöpfe) entstanden sind</li>
                <li>Der Boden nach Jahrzehnten eine komplett neue Farbe oder Optik (z.B. von rotbraun auf modern-hell) erhalten soll</li>
            </ul>

            <div class="bg-[#f9f8f6] p-8 rounded-2xl border border-gray-100 my-10">
                <h3 class="text-xl font-bold text-[#ae8f73] mb-3">Fazit der Schreinerei Yacoub</h3>
                <p class="text-gray-700">Mit der richtigen, regelmäßigen Pflege hält ein hochwertiger Parkettboden ein Leben lang. Sollte Ihr Boden in der Südpfalz dennoch einmal eine Auffrischung oder einen professionellen Abschliff benötigen, stehen wir Ihnen mit unseren modernen, nahezu staubfreien Schleifmaschinen gerne zur Seite.</p>
            </div>
        """
    },
    {
        'id': 'ratgeber-dachschraegen-schrank',
        'title': 'Einbauschrank für Dachschrägen: Jeden Zentimeter nutzen',
        'category': 'Innenausbau',
        'image': '/assets/images/innenausbau-1.jpeg',
        'content': """
            <p class="text-xl text-gray-600 leading-relaxed mb-8 font-light">Dachschrägen verleihen einem Raum extreme Gemütlichkeit und Charakter – doch bei der Einrichtung treiben sie Hausbesitzer oft zur Verzweiflung. Standardmöbel verschenken wertvollen Platz oder wirken deplatziert. Ein maßgefertigter Einbauschrank ist hier oft die einzige und vor allem eleganteste Lösung.</p>
            
            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Warum Möbel von der Stange unterm Dach nicht funktionieren</h2>
            <p class="mb-8">Die Neigungswinkel von Dächern sind niemals genormt. Stellt man eine gerade Standardkommode unter eine Schräge, bleibt ein tiefes Dreieck aus ungenutztem Raum übrig – ein idealer Staubfänger. Zudem wird die optische Ruhe des Raumes gestört, da die Möbelkanten in einem harten Kontrast zu den Linien der Architektur stehen.</p>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Die Vorteile eines maßgefertigten Drempelschranks</h2>
            <p class="mb-6">Ein Drempel (Kniestock) ist die niedrige Wand unter der Dachschräge. Maßgefertigte Schränke, die sich millimetergenau in diesen Raum einpassen, bieten enorme Vorteile:</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li><strong>Maximaler Stauraum:</strong> Die volle Tiefe des Kniestocks (oft über 1 Meter) kann beispielsweise für Auszugschubladen oder Kleiderstangen genutzt werden.</li>
                <li><strong>Nahtlose Optik:</strong> Durch eine farbliche Anpassung an die Wandfarbe (z.B. in mattem Weiß) verschmilzt der Schrank mit der Wand und der Raum wirkt sofort größer und aufgeräumter.</li>
                <li><strong>Individuelle Inneneinteilung:</strong> Ob für Aktenordner im Home-Office, Winterkleidung im Schlafzimmer oder Spielzeug im Kinderzimmer – das Innenleben wird genau auf Ihre Bedürfnisse zugeschnitten.</li>
            </ul>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Clevere Details für Schrägen</h2>
            <p class="mb-8">Als Schreinerei setzen wir bei Dachschrägen oft auf spezielle Beschläge. Da herkömmliche Klapptüren unter stark geneigten Schrägen oft am Dachfenster anschlagen, empfehlen sich hier maßgefertigte Schiebetüren oder Push-to-Open-Schubladen (Vollauszüge), die ohne Griffe auskommen und so die minimalistische Optik unterstreichen.</p>

            <div class="bg-[#f9f8f6] p-8 rounded-2xl border border-gray-100 my-10">
                <h3 class="text-xl font-bold text-[#ae8f73] mb-3">Planen Sie Ihr Projekt in Landau</h3>
                <p class="text-gray-700">Haben Sie einen Raum mit Dachschräge, den Sie bisher kaum nutzen können? Wir kommen gerne bei Ihnen in der Südpfalz vorbei, nehmen Aufmaß mittels moderner Lasertechnik und entwerfen einen Einbauschrank, der Ihnen jeden Zentimeter als wertvollen Stauraum zurückgibt.</p>
            </div>
        """
    },
    {
        'id': 'ratgeber-massivholz-furnier',
        'title': 'Massivholz oder Furnier? Material für Ihre Möbel',
        'category': 'Möbelbau',
        'image': '/assets/images/moebelbau-1.jpeg',
        'content': """
            <p class="text-xl text-gray-600 leading-relaxed mb-8 font-light">Wer sich vom Schreiner ein Möbelstück anfertigen lässt, steht unweigerlich vor der Frage: Soll es aus massivem Holz oder mit einem edlen Furnier gefertigt werden? Beide Materialien haben in der modernen Tischlerei ihre absolute Berechtigung. Wir erklären die Unterschiede.</p>
            
            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Was ist Massivholz?</h2>
            <p class="mb-6">Ein Möbelstück aus Massivholz besteht – wie der Name sagt – durchgehend aus demselben Holz. Die Bretter (Leimhölzer) werden direkt aus dem Baumstamm gesägt.</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li><strong>Vorteile:</strong> Massivholz ist extrem langlebig, robust und kann bei Beschädigungen problemlos mehrfach abgeschliffen und neu geölt werden. Es reguliert das Raumklima und wirkt antibakteriell.</li>
                <li><strong>Herausforderungen:</strong> Holz "arbeitet". Bei starken Temperatur- und Feuchtigkeitsschwankungen kann es sich verziehen. Für sehr große, völlig glatte Flächen (wie eine 3 Meter lange Schranktür) ist es daher konstruktiv schwierig einzusetzen.</li>
            </ul>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Was ist Echtholzfurnier?</h2>
            <p class="mb-6">Beim Furnieren wird ein extrem dünnes Blatt echten Holzes (meist 0,6 bis 2 mm dick) auf ein Trägermaterial (wie MDF oder Tischlerplatte) geleimt.</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li><strong>Vorteile:</strong> Furnierte Möbel sind "formstabil". Da das Trägermaterial nicht arbeitet, bleiben auch riesige Schrankfronten absolut gerade. Außerdem können sehr seltene, teure Edelhölzer (wie Palisander oder Wurzelholz) ressourcenschonend eingesetzt werden, da aus einem Stamm hunderte Quadratmeter Furnier gewonnen werden.</li>
                <li><strong>Herausforderungen:</strong> Das Furnier ist dünn. Ein tiefgehender Kratzer kann das darunterliegende Trägermaterial freilegen. Massives Abschleifen wie bei Massivholz ist hier nicht möglich.</li>
            </ul>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Wann wählt man was?</h2>
            <p class="mb-8">Die Entscheidung hängt maßgeblich vom Möbeltyp ab. Für einen hoch beanspruchten Esstisch, der Rempler und Kinderbesteck aushalten muss, ist Massivholz die erste Wahl (oft Eiche oder Kernbuche). Für ein minimalistisches, deckenhohes Sideboard mit absolut geraden Fronten greift der moderne Schreiner eher zu hochwertig furnierten Plattenwerkstoffen.</p>

            <div class="bg-[#f9f8f6] p-8 rounded-2xl border border-gray-100 my-10">
                <h3 class="text-xl font-bold text-[#ae8f73] mb-3">Beratung in unserer Werkstatt</h3>
                <p class="text-gray-700">Oft ist auch eine Kombination die beste Lösung (z.B. furnierter Korpus, massive Kanten und Arbeitsplatten). Besuchen Sie uns in unserer Schreinerei Yacoub in Landau – wir zeigen Ihnen gerne Musterbretter beider Verarbeitungsarten.</p>
            </div>
        """
    },
    {
        'id': 'ratgeber-moebel-restaurieren',
        'title': 'Alte Holzmöbel restaurieren lassen: Wann lohnt sich das?',
        'category': 'Restauration',
        'image': '/assets/images/restauration-1.jpeg',
        'content': """
            <p class="text-xl text-gray-600 leading-relaxed mb-8 font-light">Ein alter Biedermeier-Sekretär auf dem Dachboden oder der wackelige Esstisch der Großeltern: Oft zögern Besitzer, alte Holzmöbel aufarbeiten zu lassen. Die Frage lautet: Lohnt sich die Restauration finanziell und qualitativ, oder sollte man lieber neu kaufen?</p>
            
            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Qualität, die man heute nicht mehr (bezahlen) kann</h2>
            <p class="mb-8">Die meisten antiken Möbel wurden für die Ewigkeit gebaut. Damals wurden Holzverbindungen wie Zinken und Zapfen per Hand geschlagen, Holz wurde über Jahre langsam an der Luft getrocknet (nicht in Tagen im Trockenofen), und es wurden wertvolle Massivhölzer verarbeitet. Wenn Sie ein solches Möbelstück heute in gleicher Qualität von Grund auf neu anfertigen lassen würden, läge der Preis oft um ein Vielfaches höher als die Kosten einer professionellen Restauration.</p>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Was kann überhaupt restauriert werden?</h2>
            <p class="mb-6">Viele vermeintliche Totalschäden lassen sich durch fachmännisches Handwerk beheben:</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li><strong>Wackelige Konstruktionen:</strong> Alter Knochenleim verliert irgendwann seine Bindekraft. Ein Stuhl, der auseinanderzufallen droht, wird von uns zerlegt, gereinigt und neu verleimt – danach ist er wieder stabil wie am ersten Tag.</li>
                <li><strong>Holzwurmbefall:</strong> Löcher von Insekten bedeuten nicht das Ende. Nach einer giftfreien Wärmebehandlung können Fehlstellen oft so ausgebessert werden, dass die Stabilität und Optik wiederhergestellt sind.</li>
                <li><strong>Stumpfe, fleckige Oberflächen:</strong> Ein alter, grauer Lack kann behutsam entfernt (abgewaschen) werden. Durch eine neue Handpolitur mit Schellack oder Öl kommt die oft atemberaubende Original-Maserung des Holzes wieder zum Vorschein.</li>
            </ul>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Nachhaltigkeit und Werterhalt</h2>
            <p class="mb-8">Möbelrestauration ist die ursprünglichste Form der Nachhaltigkeit. Anstatt einen billigen Pressspan-Schrank zu kaufen, der in fünf Jahren auf dem Sperrmüll landet, bewahren Sie ein Stück Kulturgeschichte. Gleichzeitig steigt der finanzielle Wert eines fachgerecht aufgearbeiteten Antikmöbels meist deutlich an.</p>

            <div class="bg-[#f9f8f6] p-8 rounded-2xl border border-gray-100 my-10">
                <h3 class="text-xl font-bold text-[#ae8f73] mb-3">Unverbindliche Einschätzung</h3>
                <p class="text-gray-700">Sie sind sich unsicher? Schicken Sie uns ein paar Fotos Ihres Möbels oder vereinbaren Sie einen Termin im Raum Landau. Wir geben Ihnen eine ehrliche und transparente Einschätzung über den Aufwand und die zu erwartenden Kosten einer Aufarbeitung.</p>
            </div>
        """
    },
    {
        'id': 'ratgeber-holzfenster-sanieren',
        'title': 'Holzfenster sanieren oder tauschen? Ratgeber für Altbauten',
        'category': 'Türen & Fenster',
        'image': '/assets/images/tueren-fenster-1.jpeg',
        'content': """
            <p class="text-xl text-gray-600 leading-relaxed mb-8 font-light">Echte Holzfenster prägen das Gesicht eines historischen Altbaus wie kein anderes architektonisches Element. Doch wenn die Heizkosten steigen und es zieht, stehen viele Besitzer in der Pfalz vor der Frage: Die alten Original-Fenster aufarbeiten oder doch gegen neue austauschen?</p>
            
            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Warum Holzfenster sanieren oft die bessere Wahl ist</h2>
            <p class="mb-8">Gerade bei Gebäuden aus der Gründerzeit oder dem Jugendstil (wie sie in Landau und Neustadt häufig vorkommen), wurden oft extrem dichte, feinjährige Hölzer (z.B. Pitchpine oder abgelagertes Eichenholz) verwendet. Diese Holzqualität ist auf dem heutigen Markt kaum noch bezahlbar. Ein Austausch gegen moderne Standard-Kunststofffenster zerstört nicht nur die historische Fassadenoptik, sondern führt in Altbauten ohne moderne Lüftungskonzepte oft zu Schimmelbildung, da Kunststofffenster komplett abdichten.</p>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Wie werden alte Fenster energetisch aufgewertet?</h2>
            <p class="mb-6">Man muss nicht frieren, um Denkmalschutz zu betreiben. Es gibt hervorragende schreinerische Methoden, alte Fenster technisch in die Gegenwart zu holen:</p>
            <ul class="list-disc pl-6 mb-8 space-y-3 text-gray-700">
                <li><strong>Einfräsen von Silikondichtungen:</strong> Zugluft entsteht meist, weil alte Fensterflügel über die Jahrzehnte minimal verzogen sind und keine Dichtungslippe besitzen. Wir fräsen nachträglich eine Nut ein und integrieren moderne, unsichtbare Silikondichtungen.</li>
                <li><strong>Isolierglas-Umrüstung:</strong> Wenn der Rahmen noch dick und stabil genug ist, können wir die alte Einfachverglasung oft durch spezielles, dünnes Isolierglas (oder sogenanntes Vakuumglas) ersetzen, ohne dass die historische Optik der Sprossen leidet.</li>
                <li><strong>Flügelüberarbeitung:</strong> Klemmende oder hängende Flügel werden von uns gangbar gemacht, Wetterschenkel ausgetauscht und das Holz neu geschliffen und gestrichen.</li>
            </ul>

            <h2 class="text-3xl font-bold text-[#1a1a1a] mt-12 mb-6">Wann ein Austausch unvermeidlich ist</h2>
            <p class="mb-8">Ist das Holz in den Ecken bereits völlig verfault oder die Substanz durch jahrzehntelange Vernachlässigung zerstört, hilft oft nur der Neukauf. Aber auch hier gibt es Lösungen: Als Schreinerei können wir historische Fenster originalgetreu aus modernem Holz, mit denkmalgerechten Profilen und modernster Dreifachverglasung nachbauen.</p>

            <div class="bg-[#f9f8f6] p-8 rounded-2xl border border-gray-100 my-10">
                <h3 class="text-xl font-bold text-[#ae8f73] mb-3">Fenstercheck in der Südpfalz</h3>
                <p class="text-gray-700">Bevor Sie sich entscheiden, lassen Sie einen Fachmann draufschauen. Die Schreinerei Yacoub berät Sie kompetent vor Ort, welche Maßnahme für Ihre Fenster wirtschaftlich und bauphysikalisch den meisten Sinn ergibt.</p>
            </div>
        """
    }
]

template_article = """
    <!-- Article Header -->
    <section class="pt-40 pb-20 bg-[#f9f8f6]">
        <div class="container mx-auto px-4 max-w-4xl text-center">
            <div class="inline-block bg-[#ae8f73] text-white text-xs font-bold uppercase tracking-widest py-1.5 px-3 rounded-full mb-6">
                {category}
            </div>
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-light text-[#1a1a1a] mb-8 leading-tight tracking-tight">
                {title}
            </h1>
            <div class="flex items-center justify-center gap-4 text-gray-500 text-sm">
                <span class="font-semibold text-[#242424]">Schreinerei Yacoub</span>
                <span class="w-1 h-1 rounded-full bg-gray-300"></span>
                <span>Ratgeber</span>
            </div>
        </div>
    </section>

    <!-- Article Image -->
    <section class="bg-[#f9f8f6] pb-16">
        <div class="container mx-auto px-4 max-w-5xl">
            <div class="rounded-3xl overflow-hidden shadow-2xl h-[400px] md:h-[500px]">
                <img src="{image}" alt="{title}" class="w-full h-full object-cover">
            </div>
        </div>
    </section>

    <!-- Article Content -->
    <section class="py-16 bg-white">
        <div class="container mx-auto px-4 max-w-3xl">
            <div class="prose prose-lg prose-[#ae8f73] max-w-none text-[#242424]">
                {content}
            </div>
            
            <div class="mt-16 pt-10 border-t border-gray-200">
                <a href="/ratgeber.html" class="inline-flex items-center text-[#ae8f73] font-bold tracking-widest uppercase hover:text-[#1a1a1a] transition-colors">
                    <span class="mr-2">←</span> Zurück zur Übersicht
                </a>
            </div>
        </div>
    </section>
"""

# Generate 5 Article Pages
for article in articles_data:
    filename = f"{article['id']}.html"
    
    # Correct Title in head
    page_head = head.replace(
        '<title>Türen & Fensterbau Landau – Holztüren vom Schreiner | Schreinerei Yacoub</title>',
        f'<title>{article["title"]} | Schreinerei Yacoub</title>'
    )
    # Simple replace description
    page_head = re.sub(
        r'<meta name="description" content="[^"]+">',
        f'<meta name="description" content="{article["title"]} – Expertenwissen der Schreinerei Yacoub in Landau in der Pfalz.">',
        page_head
    )
    
    body = template_article.format(
        title=article['title'],
        category=article['category'],
        image=article['image'],
        content=article['content']
    )
    
    html_content = f"<!DOCTYPE html>\n<html lang=\"de\" class=\"scroll-smooth\">\n{page_head}\n<body class=\"font-['Inter'] text-[#242424] antialiased selection:bg-[#ae8f73] selection:text-white\">\n{header}\n{body}\n{footer}"
    
    with open(filename, 'w') as f:
        f.write(html_content)
        
    print(f"Created {filename}")

