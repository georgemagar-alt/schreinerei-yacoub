with open('bodenarbeiten.html', 'r') as f:
    content = f.read()

# Replace images and add lazy loading
# 01
content = content.replace(
    '<img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Parkett verlegen" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]">',
    '<img src="/assets/images/bodenarbeiten-parkett.jpeg" alt="Parkett verlegen" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]" loading="lazy">'
)

# 02
content = content.replace(
    '<img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Vinyl verlegen" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]">',
    '<img src="/assets/images/bodenarbeiten-vinyl.jpeg" alt="Vinyl verlegen" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]" loading="lazy">'
)

# 03
content = content.replace(
    '<img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Laminat verlegen" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]">',
    '<img src="/assets/images/bodenarbeiten-laminat.jpeg" alt="Laminat verlegen" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]" loading="lazy">'
)

# 04
content = content.replace(
    '<img src="/assets/images/tea,-schreineri-yacoub.jpeg" alt="Bodenrenovierung" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]">',
    '<img src="/assets/images/bodenarbeiten.jpeg" alt="Bodenrenovierung" class="w-full object-cover h-[500px] lg:h-[700px] shadow-2xl filter contrast-[1.05]" loading="lazy">'
)

with open('bodenarbeiten.html', 'w') as f:
    f.write(content)
