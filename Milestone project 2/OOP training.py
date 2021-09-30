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

coor1 = (5,10)
coor2 = (7,9)

li = Line (coor1,coor2)

print (li.distance())
print (li.slope())
