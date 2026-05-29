import re

with open('tueren-fenster.html', 'r') as f:
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

# Custom Body
body = """
    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 md:pt-48 md:pb-32 overflow-hidden bg-[#1a1a1a]">
        <div class="absolute inset-0 z-0 opacity-40">
            <img src="/assets/images/massanfertigung-1.jpeg" alt="Ratgeber Schreinerei Yacoub" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-[#1a1a1a] via-transparent to-transparent"></div>
        </div>
        
        <div class="container mx-auto px-4 max-w-7xl relative z-10 text-center">
            <div class="flex items-center justify-center gap-4 mb-6">
                <div class="w-12 h-[2px] bg-[#ae8f73]"></div>
                <span class="text-[#ae8f73] font-bold tracking-widest uppercase text-sm">Wissen & Tipps</span>
                <div class="w-12 h-[2px] bg-[#ae8f73]"></div>
            </div>
            <h1 class="text-5xl md:text-6xl lg:text-7xl font-light text-white mb-8 leading-[1.1] tracking-tight">
                Der Schreinerei <br><span class="font-bold">Ratgeber</span>
            </h1>
            <p class="text-xl text-gray-300 mb-0 max-w-2xl mx-auto leading-relaxed font-light">
                Expertenwissen, Pflegehinweise und Inspirationen direkt vom Schreinermeister für Ihr Zuhause in der Südpfalz.
            </p>
        </div>
    </section>

    <!-- Articles Grid Section -->
    <section class="py-24 bg-[#f9f8f6]">
        <div class="container mx-auto px-4 max-w-7xl">
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                
                <!-- Article 1 -->
                <article class="bg-white rounded-2xl overflow-hidden shadow-[0_10px_30px_-10px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group flex flex-col h-full border border-gray-100">
                    <div class="h-64 overflow-hidden relative">
                        <img src="/assets/images/bodenarbeiten.jpeg" alt="Parkett pflegen" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute top-4 left-4 bg-[#ae8f73] text-white text-xs font-bold uppercase tracking-widest py-1.5 px-3 rounded-full">Bodenarbeiten</div>
                    </div>
                    <div class="p-8 flex flex-col flex-grow">
                        <h3 class="text-xl font-bold mb-4 text-[#242424] group-hover:text-[#ae8f73] transition-colors line-clamp-2">Parkett pflegen und schleifen: Tipps vom Schreinermeister</h3>
                        <p class="text-gray-600 mb-6 leading-relaxed text-sm flex-grow">Wie man geöltes vs. lackiertes Parkett pflegt, wann ein Abschliff nötig ist und warum der Fachmann das beste Ergebnis erzielt.</p>
                        <a href="#" class="inline-flex items-center text-sm font-bold text-[#1a1a1a] hover:text-[#ae8f73] uppercase tracking-widest transition-colors">
                            Artikel lesen <span class="ml-2">→</span>
                        </a>
                    </div>
                </article>

                <!-- Article 2 -->
                <article class="bg-white rounded-2xl overflow-hidden shadow-[0_10px_30px_-10px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group flex flex-col h-full border border-gray-100">
                    <div class="h-64 overflow-hidden relative">
                        <img src="/assets/images/innenausbau-1.jpeg" alt="Einbauschrank Dachschrägen" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute top-4 left-4 bg-[#ae8f73] text-white text-xs font-bold uppercase tracking-widest py-1.5 px-3 rounded-full">Innenausbau</div>
                    </div>
                    <div class="p-8 flex flex-col flex-grow">
                        <h3 class="text-xl font-bold mb-4 text-[#242424] group-hover:text-[#ae8f73] transition-colors line-clamp-2">Einbauschrank für Dachschrägen: Jeden Zentimeter nutzen</h3>
                        <p class="text-gray-600 mb-6 leading-relaxed text-sm flex-grow">Inspiration und Vorteile von maßgefertigten Schränken in verwinkelten Räumen, unterm Dach oder in schmalen Fluren.</p>
                        <a href="#" class="inline-flex items-center text-sm font-bold text-[#1a1a1a] hover:text-[#ae8f73] uppercase tracking-widest transition-colors">
                            Artikel lesen <span class="ml-2">→</span>
                        </a>
                    </div>
                </article>

                <!-- Article 3 -->
                <article class="bg-white rounded-2xl overflow-hidden shadow-[0_10px_30px_-10px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group flex flex-col h-full border border-gray-100">
                    <div class="h-64 overflow-hidden relative">
                        <img src="/assets/images/moebelbau-1.jpeg" alt="Massivholz oder Furnier" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute top-4 left-4 bg-[#ae8f73] text-white text-xs font-bold uppercase tracking-widest py-1.5 px-3 rounded-full">Möbelbau</div>
                    </div>
                    <div class="p-8 flex flex-col flex-grow">
                        <h3 class="text-xl font-bold mb-4 text-[#242424] group-hover:text-[#ae8f73] transition-colors line-clamp-2">Massivholz oder Furnier? Material für Ihre Möbel nach Maß</h3>
                        <p class="text-gray-600 mb-6 leading-relaxed text-sm flex-grow">Erklärung der Unterschiede in Haltbarkeit, Optik und Preis. Betonung der Nachhaltigkeit von echtem Massivholz.</p>
                        <a href="#" class="inline-flex items-center text-sm font-bold text-[#1a1a1a] hover:text-[#ae8f73] uppercase tracking-widest transition-colors">
                            Artikel lesen <span class="ml-2">→</span>
                        </a>
                    </div>
                </article>

                <!-- Article 4 -->
                <article class="bg-white rounded-2xl overflow-hidden shadow-[0_10px_30px_-10px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group flex flex-col h-full border border-gray-100">
                    <div class="h-64 overflow-hidden relative">
                        <img src="/assets/images/restauration-1.jpeg" alt="Möbelrestauration" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute top-4 left-4 bg-[#ae8f73] text-white text-xs font-bold uppercase tracking-widest py-1.5 px-3 rounded-full">Restauration</div>
                    </div>
                    <div class="p-8 flex flex-col flex-grow">
                        <h3 class="text-xl font-bold mb-4 text-[#242424] group-hover:text-[#ae8f73] transition-colors line-clamp-2">Alte Holzmöbel restaurieren lassen: Wann lohnt sich das?</h3>
                        <p class="text-gray-600 mb-6 leading-relaxed text-sm flex-grow">Was bei Holzwurmbefall, stumpfen Lacken oder Rissen getan werden kann und warum Erbstücke es wert sind.</p>
                        <a href="#" class="inline-flex items-center text-sm font-bold text-[#1a1a1a] hover:text-[#ae8f73] uppercase tracking-widest transition-colors">
                            Artikel lesen <span class="ml-2">→</span>
                        </a>
                    </div>
                </article>

                <!-- Article 5 -->
                <article class="bg-white rounded-2xl overflow-hidden shadow-[0_10px_30px_-10px_rgba(0,0,0,0.05)] hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.1)] transition-all duration-500 hover:-translate-y-2 group flex flex-col h-full border border-gray-100">
                    <div class="h-64 overflow-hidden relative">
                        <img src="/assets/images/tueren-fenster-1.jpeg" alt="Holzfenster sanieren" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute top-4 left-4 bg-[#ae8f73] text-white text-xs font-bold uppercase tracking-widest py-1.5 px-3 rounded-full">Türen & Fenster</div>
                    </div>
                    <div class="p-8 flex flex-col flex-grow">
                        <h3 class="text-xl font-bold mb-4 text-[#242424] group-hover:text-[#ae8f73] transition-colors line-clamp-2">Holzfenster sanieren oder tauschen? Ratgeber für Altbauten</h3>
                        <p class="text-gray-600 mb-6 leading-relaxed text-sm flex-grow">Wie man den Charme von Altbauten in der Pfalz bewahrt und trotzdem modernste Dämmwerte erreicht.</p>
                        <a href="#" class="inline-flex items-center text-sm font-bold text-[#1a1a1a] hover:text-[#ae8f73] uppercase tracking-widest transition-colors">
                            Artikel lesen <span class="ml-2">→</span>
                        </a>
                    </div>
                </article>

            </div>
        </div>
    </section>
"""

new_content = f"<!DOCTYPE html>\n<html lang=\"de\" class=\"scroll-smooth\">\n{head}\n<body class=\"font-['Inter'] text-[#242424] antialiased selection:bg-[#ae8f73] selection:text-white\">\n{header}\n{body}\n{footer}"

# Correct Title in head
new_content = new_content.replace(
    '<title>Türen & Fensterbau Landau – Holztüren vom Schreiner | Schreinerei Yacoub</title>',
    '<title>Ratgeber & Fachwissen – Schreinerei Yacoub in Landau</title>'
)
new_content = new_content.replace(
    '<meta name="description" content="Maßgefertigte Innentüren, Haustüren und Holzfenster vom Schreinermeister in Landau in der Pfalz. Funktional, langlebig und wunderschön.">',
    '<meta name="description" content="Expertenwissen, Pflegehinweise und Inspirationen rund um Möbelbau, Innenausbau und Bodenarbeiten direkt vom Schreinermeister.">'
)

with open('ratgeber.html', 'w') as f:
    f.write(new_content)
    
print("ratgeber.html created!")
