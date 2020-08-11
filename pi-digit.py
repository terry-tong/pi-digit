#pi-digit

from math import pi

precision = int(input("How many decimal places would you like to estimate Pi to? "))
while precision > 48:
    print("Sorry the number of decimal places is too large. Please")
    precision = int(input("How many decimal places would you like to estimate Pi to? "))
else:
    print (format(pi,'.'+str(precision)+'f'))