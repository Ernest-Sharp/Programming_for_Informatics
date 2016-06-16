# Exercise 3.2 Rewrite your pay program using
# try and except so that your pro- gram handles
# non-numeric input gracefully by printing a
# message and exiting the program. The following
# shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
try:
    inphour = raw_input("Enter Hours: ")
    hours = float(inphour)
    inprate = raw_input("Enter Rate: ")
    rate = float(inprate)
    if hours <= 40 and hours > 0:
        pay = float(hours) * float(rate)
    else:
        pay = (40 * float(rate)) + ((float(hours) - 40) * float(rate) * 1.5 )
    print "Pay: ", pay
except:
    print "Error, please enter numeric input"
