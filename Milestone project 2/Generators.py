#Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):

    for x in range(N):
        yield x**2

for x in gensquares(10):

    print(x)

#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
#Note: Use the random library. For example:

print('')

import random
global count

def ran_in_range(low, high, count):


    for num in range(count):

        yield random.randint(low,high)

for x in ran_in_range(5,200,5):

    print(x)

#Use the iter() function to convert the string below into an iterator:

s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))

#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

print('I have a lot of data and I do not want to create a big list')



