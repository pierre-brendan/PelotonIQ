# temp method for parsing PCS using Python

# import packages
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# start with non-looped method to get profiles
url = 'https://www.procyclingstats.com/rider/alejandro-valverde'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

# GC method
spans = soup.find_all('li', {"class": "gc"})
lines = [span.get_text() for span in spans]
print(lines)

# Classic
spans = soup.find_all('li', {"class": "classic"})
lines = [span.get_text() for span in spans]
print(lines)

# Time trial
spans = soup.find_all('li', {"class": "tt"})
lines = [span.get_text() for span in spans]
print(lines)

# Sprint
spans = soup.find_all('li', {"class": "sprint"})
lines = [span.get_text() for span in spans]
print(lines)

# Climber
spans = soup.find_all('li', {"class": "climber"})
lines = [span.get_text() for span in spans]
print(lines)

# Rider & Team
spans = soup.find_all('h1')
lines = [span.get_text() for span in spans]
rider2 = lines
rider2 = ''.join(rider2)
rider2 = re.sub("».*$", "", rider2)
rider2 = re.sub("  ", "", rider2)
print(rider2)

team2 = lines
team2 = ''.join(team2)
team2 = re.sub('$.»*', '', team2)
print(team2)
