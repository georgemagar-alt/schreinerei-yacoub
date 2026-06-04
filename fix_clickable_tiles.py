import re

with open('ratgeber.html', 'r') as f:
    content = f.read()

# Pattern captures:
# 1: <article class="
# 2: classes (excluding final quote)
# 3: "> to <a href="
# 4: URL
# 5: " class="
# 6: Link classes
# 7: "> Artikel lesen <span class="ml-2">→</span> </a> </div> </article>
pattern = re.compile(
    r'<article class="([^"]*)">\s*<div class="h-64 overflow-hidden relative">.*?<h3.*?</h3>\s*<p.*?</p>\s*<a href="([^"]+)" class="([^"]+)">\s*Artikel lesen <span class="ml-2">→</span>\s*</a>\s*</div>\s*</article>',
    re.DOTALL
)

def replacer(match):
    article_classes = match.group(1)
    url = match.group(2)
    link_classes = match.group(3)
    
    # We replace <article> with <a href="url" class="block {article_classes}">
    # and we replace the inner <a> with a <span>
    # and we replace </article> with </a>
    
    # Let's just do a string replacement on the whole matched text.
    text = match.group(0)
    
    text = text.replace(f'<article class="{article_classes}">', f'<a href="{url}" class="block {article_classes}">')
    text = text.replace('</article>', '</a>')
    
    text = text.replace(f'<a href="{url}" class="{link_classes}">', f'<span class="{link_classes}">')
    # Be careful, we just replaced the first <a href=... inside this block with <span, which is correct because the block only contains one.
    text = text.replace('</a>\n                    </div>\n                </a>', '</span>\n                    </div>\n                </a>')
    
    return text

new_content = pattern.sub(replacer, content)

with open('ratgeber.html', 'w') as f:
    f.write(new_content)

print("Tiles made clickable.")
