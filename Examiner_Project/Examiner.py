#Examiner
#--------
import time, random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

vocabulary = [['que','that'],['para','for'],['aquí','here'],['caballo','horse'],
              ['madera','wood'],['carta','letter'],['canción','song']]

class Examine:

    def __init__(self,time_value):

        self.time_value = time_value

    def countdown(self, t):
        while t > 0:
            print("\r", 'Remaining time:', t, end="")
            t -= 1
            time.sleep(1)
        print("\r", '', end="")

    def examine_me(self):
        
        rand_int = random.randint(0,len(vocabulary)-1)
        check = input(f'Translate {vocabulary[rand_int][0]} to english: ')


        if check == vocabulary[rand_int][1]:
            print("You are right !")
        else:
            print(f"No, the translation is {vocabulary[rand_int][1]}")

while True:

    first_examine = Examine(10)

    first_examine.examine_me()

#first_examine.countdown(7)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Examiner")

    win.show()
    sys.exit(app.exec_())

window()