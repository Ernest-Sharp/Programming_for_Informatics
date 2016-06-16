# Exercise 2.3 Write a program to prompt the user
# for hours and rate per hour to compute gross pay.

inthours = raw_input("Enter Hours: ")
intrate = raw_input("Enter Rate: ")
pay = float(inthours) * float(intrate)
print "Pay: ", pay
