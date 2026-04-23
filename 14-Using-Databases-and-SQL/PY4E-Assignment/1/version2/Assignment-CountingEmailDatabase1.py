import urllib.request, urllib.parse, urllib.error
import sqlite3, json, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = 'https://www.py4e.com/code3/mbox.txt'
req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, context=ctx)

with open('mbox.txt', 'wb') as fhand:
    fhand.write(html.read())

conn = sqlite3.connect('mailbox1.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

org_count = dict()

fhand = open('mbox.txt', 'r', encoding='utf-8')

for line in fhand:
    org_emails = re.findall(r'[a-zA-Z0-9]\S*@(\S*[a-zA-Z])', line)
    for org_email in org_emails:
        org_count[org_email] = org_count.get(org_email, 0) + 1
        if org_count[org_email] == 1:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org_email, org_count[org_email]))
        else:
            cur.execute('UPDATE Counts SET count = ? WHERE org = ?', (org_count[org_email], org_email))
conn.commit()

cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
for row in cur:
    print(row[0], row[1])

fhand.close()
cur.close()
conn.close()