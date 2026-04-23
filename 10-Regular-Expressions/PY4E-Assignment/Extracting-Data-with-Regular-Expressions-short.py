import re
print( sum( [ int(i) for i in re.findall('[0-9]+', open('10-Regular-Expressions/regex_sum_2393306.txt').read()) ] ) )