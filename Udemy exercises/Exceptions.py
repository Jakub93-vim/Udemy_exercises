# problem 1

try:
    for i in ['a','b','c']:
        print(i**2)

except:
    print('There is an error')

finally:
    print('')

#problem 2

try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print('You divided by zero')

finally:
    print('All done')

# problem 3
#Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

def square ():

    while True:
        try:

            num = (int(input('Give me number: ')))**2
        except:
            print('Wrong input')
            continue
        else:
            print(num)
            break


square()