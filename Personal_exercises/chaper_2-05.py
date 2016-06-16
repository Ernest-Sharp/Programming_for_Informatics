# Exercise 2.5 Write a program which prompts the
# user for a Celsius temperature, convert the
# temperature to Fahrenheit, and print out the
# converted temperature.

# Celsius a Fahrenheit (C x 9/5) + 32 = F

celsius = raw_input("Enter temperature in C: ")
fahrenheit = (float(celsius) * 9 / 5) + 32
print "F = ", fahrenheit
