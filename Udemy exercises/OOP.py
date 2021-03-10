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
