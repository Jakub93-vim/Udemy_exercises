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

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
#old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
    new_name= name[:3].capitalize() + name[3:].capitalize()
    print (new_name)

old_macdonald('oldmacdonald')

#MASTER YODA: Given a sentence, return a sentence with the words reversed¶
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    text = text.split(' ')
    new_text=''
    text_length = len(text)-1
    
    for i in range(text_length+1):
        new_text = new_text + ' ' + text[text_length-i]
    print (new_text)
    
master_yoda('I am home')


#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

def almost_there(n):
    if (n>=90 and n<=110) or (n>=190 and n<=210):
        print(True)
        return True
    else:
        print(False)
        return False

almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)

print('LEVEL 2 PROBLEMS')

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(len(nums)):
        if nums[slice(i,i+2)] == [3,3]: #slice vyvtvori objekt slice ktery vybere dve cisla za sebou
            is_33=True
            break
        else:
            is_33=False
    print (is_33)

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    


