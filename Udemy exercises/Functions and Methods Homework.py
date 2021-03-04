
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

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list (list):

    #new_list = (x for x in list if x not in list)
    new_list = []
    for x in list:
        if x in new_list:
            pass
        else:
            new_list.append(x)

    return new_list

print(unique_list([1,1,1,2,2,3,4,5,6,6,7,8,8]))
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


#Write a Python function to multiply all the numbers in a list.

def multiply (num):
    mult = 1
    #mult = [x*x for x in num]

    for x in num:
        mult = mult*x

    return mult

print(multiply([1, 2, 3, -4]))


#Write a Python function that checks whether a word or phrase is palindrome or not.



