class Dog ():

    type = 'mammel'

    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print('Woof Woof, my name is: {} and age {} '.format(self.name, number))

my_dog = Dog(breed='lab',name='Dacan',spots=True)

print(my_dog.bark(5))

class Circle():

    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(20)


print(my_circle.get_circumference())

class Square():

    def __init__(self, side):

        self.side = side

my_square = Square(side=5)

print(my_square.side)

class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

my_animal = Animal()

my_animal.who_am_i()

class Dog2(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')


my_new_dog = Dog2()

my_new_dog.eat()

import math
class Line():

    def __init__(self,coor1,coor2):
        print('This is Line calculator')
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor1[0]-self.coor2[0])**2+(self.coor1[1]-self.coor2[1])**2)

    def slope(self):
        return ((self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))

coordinate1=(3,2)
coordinate2=(8,10)

li = Line(coordinate1,coordinate2)

print()

print(li.distance())

print(li.slope())

class Cilinder:

    pi = 3.14

    def __init__(self,height=1,radius=1):
        print('Calss my Cilinder')
        self.height = height
        self.radius = radius

    def volume(self):
        print('The volume is')

        return (self.pi*self.radius**2*self.height)

    def surface(self):

        return (self.pi*self.radius**2*2 + self.pi*2*self.radius*self.height)

my_cilinder = Cilinder(2,3)

print(my_cilinder.volume())
print(my_cilinder.surface())

