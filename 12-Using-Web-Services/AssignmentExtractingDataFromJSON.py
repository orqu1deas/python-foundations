import urllib.request, urllib.error, urllib.parse
import json

URL = 'http://py4e-data.dr-chuck.net/comments_42.json'

html = urllib.request.urlopen(URL).read()

info = json.loads(html)
comments = info['comments']
total_count = 0

for comment in comments:
    name = comment['name']
    count = int(comment['count'])
    total_count += count

print(total_count)