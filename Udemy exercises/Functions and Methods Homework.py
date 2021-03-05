
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

def up_low_dict(string):

    dict = {'upper': 0, 'lower': 0}

    for x in string:
        if x.isupper():
            dict['upper']+=1
        elif x.islower():
            dict['lower']+=1
        else:
            pass
    print ('In the string are {} upper and {} lower letters'.format(dict['upper'],dict['lower']))

up_low_dict('Hello Mr. Rogers, how are you this fine Tuesday?')

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
        mult *= x

    return mult

print(multiply([1, 2, 3, -4]))


#Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(string):
    #new_string = string.replace(' ','')
    #old_string = string.replace(' ','')
    #new_string = [x for x in new_string]
    #old_string = [x for x in old_string]
    # return new_string[::-1], old_string


    return [x for x in string.replace(' ','')] == [x for x in string.replace(' ','')][::-1]



print (palindrome('nurses run'))

#Write a Python function to check whether a string is pangram or not.

print ('is pana ?')
import string

def ispana (string, alphabet=string.ascii_lowercase):

    my_string = sorted(set(string.replace(' ','')))
    alphabet = [x for x in alphabet]
    return my_string == alphabet

print (ispana('as dfds sds '))
print (ispana('the quick brown fox jumps over the lazy dog'))
