import re

def sum_file(fhand):
    suma = 0
    for line in fhand:
        line = line.strip()
        nums_str = re.findall('[0-9]+', line)
        nums = [int(i) for i in nums_str]
        suma += sum(nums)
    return suma

try:
    filename = '10-Regular-Expressions/regex_sum_2393306.txt'
    fhand = open(filename)
except:
    print('File name not found:', filename)
    quit()

suma = sum_file(fhand)
print('The sum for the sample text above is', suma)