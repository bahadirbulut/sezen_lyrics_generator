# -*- coding: utf-8 -*-
"""
get_sezen_aksu_lyrics
"""

from bs4 import BeautifulSoup
import requests

pages = [1,2,3,4,5,6,7,8]

links = []

for page in pages:
  url = 'https://sarki.alternatifim.com/sarkici/sezen-aksu/sayfa-{page}'.format(page=page)
  root_url = 'https://sarki.alternatifim.com/'

  response = requests.get(url)
  data = response.text

  soup = BeautifulSoup(data, 'html.parser')

  for link in soup.findAll('a'):
    if link.get('href').startswith('/sarkici/'):
      links.append(root_url + str(link.get('href')))

with open('sezen_lyrics.txt', 'w') as file:
  for lyrics_url in links:
    data = requests.get(lyrics_url).text
    soup = BeautifulSoup(data, 'html.parser')

    paragraph = soup.find('div', attrs={"class":"sarkisozu"}).text.split("\n")

    for line in paragraph:
      line = line.lower()
      if line.startswith('eval(') or line.startswith('exslot') or line.startswith('1945') or \
        line.startswith('[') or line == '' or line == '\r' or line.startswith('var ') or \
        line.startswith('söz:') or line.startswith('müzik:') or '😂' in line or \
        line.startswith('söz :') or line.startswith('müzik :') or line.startswith('söz-müzik') or \
        line.startswith('söz-müzik') or line.startswith('şiir :') or  line.startswith('söz - müzik:') or \
        line.startswith('comments') or line.startswith('comments') or 'function' in line or \
        'var d' in line or 's.src' in line or '(d.' in line or '}' in line or '=' in line:
        continue
      else:
        line = line.replace('       x2', '')
        line = line.replace(' (x2)', '')
        line = line.replace(' (x3)', '')
        line = line.replace('    x2', '')
        line = line.replace('    x3', '')
        line = line.replace('    x4', '')
        line = line.replace(' x2', '')
        line = line.replace(' x3', '')
        line = line.replace(' x4', '')
        line = line.replace(' (x4)', '')
        line = line.replace('(x2)', '')
        line = line.replace('     x2', '')
        file.write(line+'\n')

