import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

name = 'Amos'
pos = 18
times = 7

url = f'http://py4e-data.dr-chuck.net/known_by_{name}.html'
list_names = []

for i in range(0, times):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.find_all('a')

    name = str(a_tags[pos-1].contents[0])
    url = f'http://py4e-data.dr-chuck.net/known_by_{name}.html'

    list_names.append(name)

print(list_names)