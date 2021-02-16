st = 'Print only the words that start with s in this sentence'

for element in st.split(' '):
    if element.startswith('s') and len(element)>=2:
        print(element)

print('')

#Use range() to print all the even numbers from 0 to 10.

for i in range(0,10):
    if i%2==0:
        print(i)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list_50= [x for x in range(1,50) if x%3==0]
print (list_50)

print('')

#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for element in st.split(' '):
    if len(element)%2==0:
        print(element)

print('')

#Write a program that prints the integers from 1 to 100. But for multiples of
#three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,100):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0 and i%5!=0:
        print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    else:
        print(i)

print('')

#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

for element in st.split(' '):
    print(element[:1])

first_let=[element[:1] for element in st.split()]
print(first_let)
