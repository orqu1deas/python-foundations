import sqlite3

conn = sqlite3.connect('track.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
''')

cur.execute('CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE)')
cur.execute('CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)')


fhand = open('tracks.csv')

for line in fhand:
    elems = line.split(',')
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (elems[1],))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (elems[1],))
    id_art = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (elems[-1],))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (elems[-1],))
    id_genre = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)', (id_art, elems[2]))
    cur.execute('SELECT id FROM Album WHERE title = ?', (elems[2],))
    id_album = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)',
                (elems[0], id_album, id_genre, elems[3], elems[4], elems[5]))

conn.commit()


sqlstr = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''
for row in cur.execute(sqlstr):
    print(row[0], row[1], row[2], row[3])

cur.close()
conn.close()