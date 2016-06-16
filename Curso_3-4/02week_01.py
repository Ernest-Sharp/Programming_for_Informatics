# In this assignment you will read through and parse a
# file with text and numbers. You will extract all the
# numbers in the file and compute the sum of the numbers.

import re
result_list= list()
result = 0
handler = open("regex_sum_206751.txt")
for line in handler:
    num_list = re.findall("[0-9]+", line)
    for num in num_list:
        result_list.append(num)
for num in result_list:
    result += int(num)
print result

