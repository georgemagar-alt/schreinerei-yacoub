import re

with open('tueren-fenster.html', 'r') as f:
    content = f.read()

# Replace Hero Section
hero_old = """    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 md:pt-48 md:pb-32 overflow-hidden">
        <div class="absolute inset-0 z-0">
            <img src="/assets/images/bodenarbeiten.jpeg" alt="Bodenarbeiten Schreinerei Yacoub" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-r from-[#1a1a1a]/95 via-[#1a1a1a]/80 to-transparent"></div>
        </div>
        
        <div class="container mx-auto px-4 max-w-7xl relative z-10">
            <div class="max-w-3xl">
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-[2px] bg-[#ae8f73]"></div>
                    <span class="text-[#ae8f73] font-bold tracking-widest uppercase text-sm">Leistungen</span>
                </div>
                <h1 class="text-5xl md:text-6xl lg:text-7xl font-light text-white mb-8 leading-[1.1] tracking-tight">
                    Bodenarbeiten in <br><span class="font-bold">Landau in der Pfalz</span>
                </h1>
                <p class="text-xl text-gray-300 mb-12 max-w-2xl leading-relaxed font-light">
                    Böden mit Stil, Präzision & Charakter. Entdecken Sie handwerkliche Qualität, die man sieht, spürt und jeden Tag genießt.
                </p>
                
                <div class="flex flex-col sm:flex-row gap-6">
                    <a href="#kontakt" class="inline-flex items-center justify-center px-8 py-4 bg-[#ae8f73] text-white font-bold tracking-wide uppercase text-sm hover:bg-white hover:text-[#1a1a1a] transition-colors duration-300">
                        Angebot anfordern
                    </a>
                </div>
            </div>
        </div>
    </section>"""

hero_new = """    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 md:pt-48 md:pb-32 overflow-hidden">
        <div class="absolute inset-0 z-0">
            <img src="/assets/images/tueren-fenster-2.jpeg" alt="Türen und Fensterbau Schreinerei Yacoub" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-r from-[#1a1a1a]/95 via-[#1a1a1a]/80 to-transparent"></div>
        </div>
        
        <div class="container mx-auto px-4 max-w-7xl relative z-10">
            <div class="max-w-3xl">
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-[2px] bg-[#ae8f73]"></div>
                    <span class="text-[#ae8f73] font-bold tracking-widest uppercase text-sm">Leistungen</span>
                </div>
                <h1 class="text-5xl md:text-6xl lg:text-7xl font-light text-white mb-8 leading-[1.1] tracking-tight">
                    Türen & Fenster in <br><span class="font-bold">Landau in der Pfalz</span>
                </h1>
                <p class="text-xl text-gray-300 mb-12 max-w-2xl leading-relaxed font-light">
                    Funktional. Langlebig. Schön. Maßgefertigte Türen und Fensterrahmen vom Schreinermeister für Ihr Zuhause.
                </p>
                
                <div class="flex flex-col sm:flex-row gap-6">
                    <a href="#kontakt" class="inline-flex items-center justify-center px-8 py-4 bg-[#ae8f73] text-white font-bold tracking-wide uppercase text-sm hover:bg-white hover:text-[#1a1a1a] transition-colors duration-300">
                        Angebot anfordern
                    </a>
                </div>
            </div>
        </div>
    </section>"""

content = content.replace(hero_old, hero_new)

# Replace Intro Section
intro_old = """    <!-- Intro Section -->
    <section class="py-24 bg-[#f9f8f6]">
        <div class="container mx-auto px-4 max-w-7xl">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-start">
                <div>
                    <h2 class="text-3xl md:text-5xl font-light mb-8 text-[#1a1a1a] leading-tight tracking-tight">
                        Neue Böden – neues Wohngefühl <br><span class="font-bold">vom Schreinermeister</span>
                    </h2>
                </div>
                <div class="space-y-6 text-lg text-gray-600 leading-relaxed font-light">
                    <p>
                        Ein Boden ist mehr als ein Belag – er ist die Bühne Ihres Wohnraums. Er verbindet Räume, trägt Möbel, schafft Atmosphäre und Komfort. Mit der Schreinerei Yacoub in Landau erhalten Sie handwerklich verlegte Böden, die Qualität und Design vereinen.
                    </p>
                    <p>
                        Wir beraten Sie individuell, liefern das passende Material und sorgen für eine saubere, präzise Verlegung – für Privatwohnungen, Büros oder ganze Objekte.
                    </p>
                </div>
            </div>
        </div>
    </section>"""

intro_new = """    <!-- Intro Section -->
    <section class="py-24 bg-[#f9f8f6]">
        <div class="container mx-auto px-4 max-w-7xl">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-start">
                <div>
                    <h2 class="text-3xl md:text-5xl font-light mb-8 text-[#1a1a1a] leading-tight tracking-tight">
                        Türen & Fenster – Stil und <br><span class="font-bold">Funktion im Einklang</span>
                    </h2>
                </div>
                <div class="space-y-6 text-lg text-gray-600 leading-relaxed font-light">
                    <p>
                        Türen und Fenster sind mehr als nur Bauelemente – sie verbinden Räume, schaffen Atmosphäre und prägen den Charakter eines Hauses. Bei der Schreinerei Yacoub aus Landau entstehen Holztüren und Fensterrahmen, die Ästhetik, Qualität und Funktion perfekt vereinen.
                    </p>
                    <p>
                        Ob moderne Innentüren, maßgefertigte Haustüren oder Fensterrahmen aus Holz – wir fertigen und montieren individuell nach Ihren Vorstellungen, millimetergenau und in echter Schreinerqualität.
                    </p>
                </div>
            </div>
        </div>
    </section>"""

content = content.replace(intro_old, intro_new)

with open('tueren-fenster.html', 'w') as f:
    f.write(content)
