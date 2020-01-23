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
