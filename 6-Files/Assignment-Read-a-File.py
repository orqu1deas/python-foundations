'''
7.1 Write a program that prompts for a file name, then opens
that file and reads through the file, and print the contents
of the file in upper case. Use the file words.txt to produce
the output below.
'''

fname = input('Enter file name: ')
try:
    fhand = open('6-Files/'+ fname)
    for line in fhand:
        print(line.strip().upper())
except:
    print('Enter a valid file name.')
    quit()