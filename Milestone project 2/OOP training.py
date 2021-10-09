import math

class Line:

    def __init__(self, coor1, coor2):
        pass

    def distance(self):

        dist = math.sqrt((coor1[1]-coor2[1])**2+((coor1[0]-coor2[0])**2))

        return dist

    def slope (self):

        slop = (coor1[1]-coor2[1])/(coor1[0]-coor2[0])

        return slop

class Cylinder:

    def __init__(self, height, rad):
        pass

    def volume(self):

        vol = math.pi*rad**2

        return vol

    def area(self):

        are = math.pi*rad*2

        return are



coor1 = (3,2)
coor2 = (8,10)

li = Line (coor1,coor2)

print (li.distance())
print (li.slope())

height = 2
rad = 3
c = Cylinder (height,rad)
print ('Volume is ', c.volume())
print ('Area is ', c.area())
