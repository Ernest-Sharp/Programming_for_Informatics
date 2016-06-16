# Exercise 3.1 Rewrite your pay computation to give
# the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
# Enter Hours: 45 Enter Rate: 10 Pay: 475.0

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
if hours <= 40 and hours > 0:
    pay = float(hours) * float(rate)
else:
    pay = (40 * float(rate)) + ((float(hours) - 40) * float(rate) * 1.5 )
print "Pay: ", pay
