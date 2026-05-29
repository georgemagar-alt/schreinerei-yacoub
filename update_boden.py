import re

with open('bodenarbeiten.html', 'r') as f:
    content = f.read()

header_end = content.find('</header>') + len('</header>')
contact_start = content.find('<!-- Contact & Form Section -->')

if header_end == -1 or contact_start == -1:
    print("Could not find markers")
    exit(1)

new_content = """

    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 md:pt-48 md:pb-32 overflow-hidden">
        <div class="absolute inset-0 z-0">
            <img src="/assets/images/hero-image-homepage.jpeg" alt="Bodenarbeiten Schreinerei Yacoub" class="w-full h-full object-cover">
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
    </section>

    <!-- Intro Section -->
    <section class="py-24 bg-white">
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
    </section>

    <!-- Services Details (Alternating Layout) -->
    <section class="py-24 bg-[#f9f8f6]">
        <div class="container mx-auto px-4 max-w-7xl">
            <div class="text-center mb-20">
                <h2 class="text-sm font-bold text-[#ae8f73] uppercase tracking-[0.2em] mb-4">Portfolio</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-[#1a1a1a] tracking-tight">Unsere Leistungen im Überblick</h3>
            </div>

            <div class="space-y-32">
                <!-- Parkett -->
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    <div class="lg:w-1/2 relative">
                        <div class="absolute -inset-4 bg-[#ae8f73]/10 rounded-3xl -z-10 transform rotate-2"></div>
                        <img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Parkett verlegen" class="rounded-2xl shadow-xl w-full object-cover h-[400px]">
                    </div>
                    <div class="lg:w-1/2">
                        <h4 class="text-3xl font-bold mb-6 text-[#1a1a1a]">Parkett verlegen & renovieren</h4>
                        <p class="text-gray-600 mb-8 text-lg leading-relaxed">Echtholzparkett ist zeitlos und edel – und ein echtes Stück Natur unter den Füßen. Wir verlegen Stabparkett, Mosaikparkett und Landhausdielen, schleifen alte Böden ab, entfernen Kratzer und behandeln sie neu mit Öl oder Lack.</p>
                        <ul class="space-y-4">
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Edle Optik & natürliche Haptik</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Langlebig & mehrfach renovierbar</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Ideal für Fußbodenheizung</li>
                        </ul>
                    </div>
                </div>

                <!-- Vinyl -->
                <div class="flex flex-col lg:flex-row-reverse items-center gap-16">
                    <div class="lg:w-1/2 relative">
                        <div class="absolute -inset-4 bg-[#ae8f73]/10 rounded-3xl -z-10 transform -rotate-2"></div>
                        <img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Vinyl verlegen" class="rounded-2xl shadow-xl w-full object-cover h-[400px]">
                    </div>
                    <div class="lg:w-1/2">
                        <h4 class="text-3xl font-bold mb-6 text-[#1a1a1a]">Vinyl- & Designböden</h4>
                        <p class="text-gray-600 mb-8 text-lg leading-relaxed">Vinyl ist pflegeleicht, robust und vielseitig. Ob in Holz-, Stein- oder Betonoptik – wir verlegen Klick-Vinyl oder Designböden, die Feuchtigkeit und Alltagsbelastung mühelos standhalten.</p>
                        <ul class="space-y-4">
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Wasserfest & strapazierfähig</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Große Dekorauswahl</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Für Küche, Bad & Gewerbe geeignet</li>
                        </ul>
                    </div>
                </div>

                <!-- Laminat & Teppich -->
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    <div class="lg:w-1/2 relative">
                        <div class="absolute -inset-4 bg-[#ae8f73]/10 rounded-3xl -z-10 transform rotate-2"></div>
                        <img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Laminat verlegen" class="rounded-2xl shadow-xl w-full object-cover h-[400px]">
                    </div>
                    <div class="lg:w-1/2">
                        <h4 class="text-3xl font-bold mb-6 text-[#1a1a1a]">Laminat & Teppichboden</h4>
                        <p class="text-gray-600 mb-8 text-lg leading-relaxed">Laminat überzeugt durch modernes Design und günstigen Preis, während wir auf optimale Trittschalldämmung und saubere Übergänge achten. Für weichere Ansprüche bieten wir fachgerecht verlegte Teppichböden, die gemütlich, trittschalldämmend und pflegeleicht sind.</p>
                        <ul class="space-y-4">
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Preiswert & schnell verlegt (Laminat)</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Kratzfest & robust</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Warme, gemütliche Haptik (Teppich)</li>
                        </ul>
                    </div>
                </div>

                <!-- Kork, Linoleum & Renovierung -->
                <div class="flex flex-col lg:flex-row-reverse items-center gap-16">
                    <div class="lg:w-1/2 relative">
                        <div class="absolute -inset-4 bg-[#ae8f73]/10 rounded-3xl -z-10 transform -rotate-2"></div>
                        <img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Bodenrenovierung" class="rounded-2xl shadow-xl w-full object-cover h-[400px]">
                    </div>
                    <div class="lg:w-1/2">
                        <h4 class="text-3xl font-bold mb-6 text-[#1a1a1a]">Bodenrenovierung & Spezialböden</h4>
                        <p class="text-gray-600 mb-8 text-lg leading-relaxed">Neben nachhaltigem Kork, Linoleum und PVC schleifen, spachteln und versiegeln wir auch Ihre vorhandenen Parkett- oder Dielenböden. Wir bringen alte Böden wieder in Topform – staubarm und mit modernster Technik.</p>
                        <ul class="space-y-4">
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Parkett in mehreren Gängen abschleifen</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Fugen spachteln & ausbessern</li>
                            <li class="flex items-center text-gray-700"><span class="w-2 h-2 bg-[#ae8f73] rounded-full mr-4"></span> Versiegeln oder Ölen für perfekten Glanz</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="py-24 bg-[#1a1a1a] text-white">
        <div class="container mx-auto px-4 max-w-7xl">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-8 border-b border-white/10 pb-8">
                <div class="max-w-2xl">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-8 h-[1px] bg-[#ae8f73]"></div>
                        <span class="text-[#ae8f73] uppercase tracking-widest text-xs font-bold">Der Weg zum neuen Boden</span>
                    </div>
                    <h2 class="text-3xl md:text-5xl font-light tracking-tight">Unser Ablauf</h2>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
                <div class="border-t border-white/10 pt-8">
                    <div class="text-4xl font-light text-[#ae8f73] mb-6">01.</div>
                    <h4 class="text-xl font-bold mb-4">Beratung</h4>
                    <p class="text-gray-400 text-sm leading-relaxed">Wir zeigen Ihnen Muster, erklären Unterschiede zwischen Materialien und helfen bei der Auswahl.</p>
                </div>
                <div class="border-t border-white/10 pt-8">
                    <div class="text-4xl font-light text-[#ae8f73] mb-6">02.</div>
                    <h4 class="text-xl font-bold mb-4">Untergrund prüfen</h4>
                    <p class="text-gray-400 text-sm leading-relaxed">Wir prüfen Feuchtigkeit, Ebenheit und Festigkeit – für ein dauerhaft gutes Ergebnis.</p>
                </div>
                <div class="border-t border-white/10 pt-8">
                    <div class="text-4xl font-light text-[#ae8f73] mb-6">03.</div>
                    <h4 class="text-xl font-bold mb-4">Verlegung</h4>
                    <p class="text-gray-400 text-sm leading-relaxed">Wir verlegen fachgerecht, schneiden präzise zu und setzen Sockelleisten oder Übergangsprofile.</p>
                </div>
                <div class="border-t border-white/10 pt-8">
                    <div class="text-4xl font-light text-[#ae8f73] mb-6">04.</div>
                    <h4 class="text-xl font-bold mb-4">Übergabe</h4>
                    <p class="text-gray-400 text-sm leading-relaxed">Nach der Verlegung reinigen wir die Fläche, prüfen die Qualität und geben Pflegetipps mit.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-4 max-w-3xl">
            <div class="text-center mb-16">
                <h2 class="text-sm font-bold text-[#ae8f73] uppercase tracking-[0.2em] mb-4">FAQ</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-[#1a1a1a] tracking-tight">Häufig gestellte Fragen</h3>
            </div>

            <div class="space-y-4">
                <!-- FAQ Item 1 -->
                <details class="group border border-gray-200 rounded-xl bg-white [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between gap-1.5 p-6 text-[#1a1a1a]">
                        <h4 class="font-bold text-lg">Welche Bodenarten verlegen Sie?</h4>
                        <span class="relative size-5 shrink-0">
                            <svg class="absolute inset-0 size-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <svg class="absolute inset-0 size-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                        </span>
                    </summary>
                    <div class="px-6 pb-6 text-gray-600 leading-relaxed">
                        Wir verlegen Parkett, Vinyl, Laminat, Teppich, Kork, Linoleum, PVC und CV-Beläge – individuell nach Bedarf.
                    </div>
                </details>
                
                <!-- FAQ Item 2 -->
                <details class="group border border-gray-200 rounded-xl bg-white [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between gap-1.5 p-6 text-[#1a1a1a]">
                        <h4 class="font-bold text-lg">Wie lange dauert eine Bodenverlegung?</h4>
                        <span class="relative size-5 shrink-0">
                            <svg class="absolute inset-0 size-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <svg class="absolute inset-0 size-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                        </span>
                    </summary>
                    <div class="px-6 pb-6 text-gray-600 leading-relaxed">
                        Je nach Fläche und Material in der Regel 1–3 Tage.
                    </div>
                </details>

                <!-- FAQ Item 3 -->
                <details class="group border border-gray-200 rounded-xl bg-white [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between gap-1.5 p-6 text-[#1a1a1a]">
                        <h4 class="font-bold text-lg">Entfernen Sie alte Böden?</h4>
                        <span class="relative size-5 shrink-0">
                            <svg class="absolute inset-0 size-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <svg class="absolute inset-0 size-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                        </span>
                    </summary>
                    <div class="px-6 pb-6 text-gray-600 leading-relaxed">
                        Ja, wir übernehmen Demontage, Entsorgung und Untergrundvorbereitung.
                    </div>
                </details>

                <!-- FAQ Item 4 -->
                <details class="group border border-gray-200 rounded-xl bg-white [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between gap-1.5 p-6 text-[#1a1a1a]">
                        <h4 class="font-bold text-lg">Bieten Sie auch Bodenrenovierungen an?</h4>
                        <span class="relative size-5 shrink-0">
                            <svg class="absolute inset-0 size-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <svg class="absolute inset-0 size-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                        </span>
                    </summary>
                    <div class="px-6 pb-6 text-gray-600 leading-relaxed">
                        Selbstverständlich – wir schleifen, versiegeln und ölen alte Holzböden.
                    </div>
                </details>

                <!-- FAQ Item 5 -->
                <details class="group border border-gray-200 rounded-xl bg-white [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex cursor-pointer items-center justify-between gap-1.5 p-6 text-[#1a1a1a]">
                        <h4 class="font-bold text-lg">Sind Ihre Materialien für Fußbodenheizung geeignet?</h4>
                        <span class="relative size-5 shrink-0">
                            <svg class="absolute inset-0 size-5 opacity-100 group-open:opacity-0 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <svg class="absolute inset-0 size-5 opacity-0 group-open:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/></svg>
                        </span>
                    </summary>
                    <div class="px-6 pb-6 text-gray-600 leading-relaxed">
                        Ja – Parkett, Vinyl und viele Designböden sind für Fußbodenheizungen freigegeben.
                    </div>
                </details>
            </div>
        </div>
    </section>

"""

final_content = content[:header_end] + new_content + content[contact_start:]

with open('bodenarbeiten.html', 'w') as f:
    f.write(final_content)

