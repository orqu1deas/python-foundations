import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

URL = 'http://py4e-data.dr-chuck.net/comments_2393310.xml'

html = urllib.request.urlopen(URL).read()
tree = ET.fromstring(html)
comments = tree.findall('comments/comment')

suma = 0

for comment in comments:
    name = comment.find('name').text
    count = int(comment.find('count').text)
    suma += count

print('Sum:', suma)