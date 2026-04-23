import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = 'http://py4e-data.dr-chuck.net/comments_2393308.html'

fhand = urllib.request.urlopen(URL, context = ctx).read()
soup = BeautifulSoup(fhand)

span_tags = soup.find_all('span')
sum = 0
count = 0
for tag in span_tags:
    num = int(tag.contents[0].strip())
    count += 1
    sum += num

print(f'Sum: {sum}, Count: {count}')