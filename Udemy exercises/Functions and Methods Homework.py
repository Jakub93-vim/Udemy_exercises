
#Write a function that computes the volume of a sphere given its radius.
import math

def vol(radius):
    return 4/3 * math.pi * radius**3

print (vol(2))



#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(low,high,num):

    return low <= num <= high

print (ran_check(2,7,5))
print (ran_check(2,7,7))
print (ran_check(2,7,20))


#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(string):

    upper = sum(1 for x in string if x.isupper())
    lower = sum(1 for x in string if x.islower())
    return upper, lower

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

