'''
10.2 Write a program to read through the mbox-short.txt and figure
out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the
time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the
counts, sorted by hour as shown below.
'''

fname = input('Enter a file name: ')
counts = dict()
try:
    fhand = open(fname)
except:
    print('File name cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.strip().split()
    if line.strip().startswith('From ') and len(words) > 5:
        date = words[5].split(':')
        hour = date[0]
        counts[hour] = counts.get(hour, 0) + 1

# lst = [(int(key), value) for key, value in list(counts.items())]
lst = list(counts.items())
lst.sort()

for key, value in lst:
    print(key, value)