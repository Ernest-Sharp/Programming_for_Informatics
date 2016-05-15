# 5.2 Write a program that repeatedly prompts a user
#  for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number.
# Enter the numbers from the book for problem 5.1 and
# Match the desired output as shown.
# Desired Output
# Invalid input
# Maximum is 7
# Minimum is 4

maximum = 0
minimum = None

while True:
    user_inp = raw_input("Enter an integer number: ")
    if user_inp == "done":
        break
    try:
        number = int(user_inp)
    except:
        print "Invalid input"
        continue
# Setup maximum and minimum
    if maximum is None:
        maximum = number
    if minimum is None:
        minimum = number
# Review values
    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number
print "Maximum is", maximum
print "Minimum is", minimum
