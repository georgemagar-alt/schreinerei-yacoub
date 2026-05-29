import urllib.request
import re
from bs4 import BeautifulSoup

URL = 'https://yacoub-schreinerei.de/tuerbau-fensterbau-landau'

req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
except Exception as e:
    print("Failed to fetch HTML:", e)
    exit(1)

soup = BeautifulSoup(html, 'html.parser')

print("--- TEXT CONTENT ---")
for string in soup.stripped_strings:
    if len(string) > 20:
        print(string)

print("\n--- IMAGES ---")
img_tags = soup.find_all('img')
for img in img_tags:
    src = img.get('src')
    if src:
        print(src)

