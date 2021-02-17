#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        print (min(a,b))
    else:
        print( max(a,b))

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    check = text.split(' ')
    first_letter=[]
    for ele in check:
        first_letter.append(ele[0])
    if first_letter[0] == first_letter[1]:
        return True
    else:
        return False

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
#or if one of the integers is 20. If not, return False


def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        print (True)
    else:
        print (False)

makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)


