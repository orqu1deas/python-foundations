import urllib.request, urllib.parse, urllib.error
import sqlite3, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = 'https://www.py4e.com/code3/mbox.txt'
req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, context=ctx)

with open('mbox.txt', 'wb') as fhand:
    fhand.write(html.read())

conn = sqlite3.connect('mailbox.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fhand = open('mbox.txt', encoding='utf-8')

for line in fhand:
    if not line.startswith('From: '):
        continue

    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
conn.close()