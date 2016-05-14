# 3.1 Write a program to prompt the user for
# hours and rate per hour using raw_input to
# compute gross pay. Pay the hourly rate for
# the hours up to 40 and 1.5 times the hourly
# rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75).
# You should use raw_input to read a string and
# float() to convert the string to a number.
# Do not worry about error checking the user
# input - assume the user types numbers properly.
# Desired Output 498.75

# Ask hours and rate
a = raw_input("Number of hours? ")
b = raw_input("Rate? ")

# Convert to float

hours = float(a)
rate = float(b)

# Check if hours > 40 and do the math

if hours > 40:
    pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
else:
    pay = hours * rate
print pay