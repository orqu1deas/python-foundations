'''
9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program
creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file. After
the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

h_emails = dict()

for line in handle:
    line = line.strip()
    if line.startswith('From'):
        words = line.split()
        email = words[1]
        h_emails[email] = h_emails.get(email, 0) + 1

max_email = None
for user in h_emails:
    if max_email == None or h_emails[user] > max_email[1]:
        max_email = [user, h_emails[user]]
print(max_email[0], max_email[1])