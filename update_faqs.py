import re
import random

cities = [
    {"slug": "landau", "short": "Landau"},
    {"slug": "neustadt", "short": "Neustadt"},
    {"slug": "speyer", "short": "Speyer"},
    {"slug": "karlsruhe", "short": "Karlsruhe"},
    {"slug": "weissenburg", "short": "Weißenburg"},
    {"slug": "frankenthal", "short": "Frankenthal"},
    {"slug": "bad-duerkheim", "short": "Bad Dürkheim"},
    {"slug": "pforzheim", "short": "Pforzheim"},
    {"slug": "kaiserslautern", "short": "Kaiserslautern"}
]

faq_pool = [
    {
        "q": "Verlegen Sie auch Böden in {city} und Umgebung?",
        "a": "Ja, wir sind als Schreinerei regelmäßig in {city} im Einsatz und verlegen Parkett, Massivholzdielen und Vinyl."
    },
    {
        "q": "Wie lange dauert es, bis ein neuer Holzboden in {city} verlegt ist?",
        "a": "Das hängt von der Raumgröße ab. Ein normales Wohnzimmer in {city} schaffen wir meist in 1-2 Tagen, inklusive Untergrundvorbereitung."
    },
    {
        "q": "Bieten Sie auch das Abschleifen von altem Parkett in {city} an?",
        "a": "Absolut! Wenn Ihr Parkett in {city} stumpf ist oder Kratzer hat, schleifen wir es professionell und nahezu staubfrei ab."
    },
    {
        "q": "Kommen Sie für ein Aufmaß kostenlos nach {city}?",
        "a": "Ja, für ein konkretes Projekt vereinbaren wir gerne einen Vor-Ort-Termin in {city}, um den Untergrund zu prüfen und exakt Maß zu nehmen."
    },
    {
        "q": "Welcher Bodenbelag eignet sich am besten für Altbauten in {city}?",
        "a": "Gerade in historischen Gebäuden in {city} empfehlen wir klassisches Massivholzparkett oder Dielen, da diese den Charme unterstreichen und sehr langlebig sind."
    },
    {
        "q": "Kann ich in meinem Neubau in {city} Parkett auf Fußbodenheizung verlegen lassen?",
        "a": "Ja, das ist heute Standard. Wir verwenden in {city} spezielle, wärmedurchlässige Kleber und vollflächige Verklebungen für maximale Heiz-Effizienz."
    },
    {
        "q": "Ist Vinylboden eine gute Alternative für Mietwohnungen in {city}?",
        "a": "Definitiv. Vinyl ist extrem strapazierfähig, pflegeleicht und lässt sich oft auch schwimmend verlegen – ideal für Mietobjekte in {city}."
    },
    {
        "q": "Entsorgen Sie auch den alten Teppich oder Laminat bei Projekten in {city}?",
        "a": "Ja, wir kümmern uns in {city} auf Wunsch um die restlose und fachgerechte Entsorgung Ihrer Altbeläge, bevor wir den neuen Boden aufbauen."
    },
    {
        "q": "Muss ich meine Möbel selbst ausräumen, wenn Sie in {city} verlegen?",
        "a": "Wir empfehlen es, können aber bei unseren Einsätzen in {city} nach Absprache auch beim Möbelrücken helfen. Sprechen Sie uns einfach bei der Planung darauf an."
    }
]

template_faq = """
    <!-- FAQ Section -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-4 max-w-3xl">
            <div class="text-center mb-16">
                <h2 class="text-sm font-bold text-[#ae8f73] uppercase tracking-[0.2em] mb-4">FAQ</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-[#1a1a1a] tracking-tight">Häufige Fragen zu Bodenarbeiten in {city}</h3>
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

random.seed(42) # Ensure reproducible results but different per city

for c in cities:
    filename = f"bodenarbeiten-{c['slug']}.html"
    
    with open(filename, 'r') as f:
        content = f.read()
        
    # Select 4 random questions for this city
    city_questions = random.sample(faq_pool, 4)
    
    faq_items_html = ""
    for i, item in enumerate(city_questions):
        q = item["q"].replace("{city}", c["short"])
        a = item["a"].replace("{city}", c["short"])
        faq_items_html += template_faq_item.format(idx=i+1, q=q, a=a) + "\n"
        
    faq_html = template_faq.format(city=c["short"], faq_items_html=faq_items_html.rstrip())
    
    # Replace block between <!-- FAQ Section --> and <!-- Contact & Form Section -->
    pattern = re.compile(r'<!-- FAQ Section -->.*?<!-- Contact & Form Section -->', re.DOTALL)
    new_content = pattern.sub(faq_html + '\n    <!-- Contact & Form Section -->', content)
    
    with open(filename, 'w') as f:
        f.write(new_content)
        
    print(f"Updated FAQ in {filename}")

