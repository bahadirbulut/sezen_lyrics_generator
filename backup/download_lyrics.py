# -*- coding: utf-8 -*-
"""
download sezen aksu song lyrics
"""

from bs4 import BeautifulSoup
import requests

pages = [1,2,3,4,5,6,7,8]

links = []

# Get the links for lyrics pages
for page in pages:
  url = 'https://sarki.alternatifim.com/sarkici/sezen-aksu/sayfa-{page}'.format(page=page)
  root_url = 'https://sarki.alternatifim.com/'

  response = requests.get(url)
  data = response.text

  soup = BeautifulSoup(data, 'html.parser')

  for link in soup.findAll('a'):
    if link.get('href').startswith('/sarkici/'):
      links.append(root_url + str(link.get('href')))

# Get the lyrics and write them to a text file
with open('sezen_lyrics.txt', 'w') as file:
  for lyrics_url in links:
    data = requests.get(lyrics_url).text
    soup = BeautifulSoup(data, 'html.parser')

    paragraph = soup.find('div', attrs={"class":"sarkisozu"}).text.split("\n")

    for line in paragraph:
      if line.startswith('eval(') or line.startswith('exslot') or \
      line.startswith('[') or line == '' or line == '\r' or line.startswith('var ') or \
      line.startswith('comments') or line.startswith('comments') or 'function' in line or \
      'var d' in line or 's.src' in line or '(d.' in line or '}' in line or '=' in line:
        continue
      else:
        file.write(line.replace('       x2', '')+'\n')

