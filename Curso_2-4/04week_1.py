# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() method. The program should build a
# list of words. For each word on each line check to see
# if the word is already in the list and if not append it
# to the list. When the program completes, sort and print
# the resulting words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

# open file
textfile = open("romeo.txt", "r")

line = list()
result = list()

# Loop file searching words
for i in textfile:
    line = i.split()
    for word in line:
        if word in result: continue  # if word is in the result list do nothing
        result.append(word)  # append new words
result.sort()  # sort list

print result