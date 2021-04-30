#Examiner
#--------


import time, random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading

vocabulary = [['que','that'],['para','for'],['aquí','here'],['caballo','horse'],
              ['madera','wood'],['carta','letter'],['canción','song']]

class Examine:

    def __init__(self):
        self.time = ''


    def countdown(self):
        self.count = 'foo'
        '''
        while t > 0:
            print("\r", 'Remaining time:', t, end="")
            t -= 1
            time.sleep(1)
        print("\r", '', end="")
        '''
        time.sleep(5)
        print('hello')
        time.sleep(1)
        print('come on')

    def examine_me(self):
        self.exa = 'fool'
        '''
        rand_int = random.randint(0,len(vocabulary)-1)
        check = input(f'Translate {vocabulary[rand_int][0]} to english: ')


        if check == vocabulary[rand_int][1]:
            print("You are right !")
        else:
            print(f"No, the translation is: {vocabulary[rand_int][1]}")
        '''

        print('the second thread')

    def run(self):

        t1 = threading.Thread(target=self.countdown)
        t2 = threading.Thread(target=self.examine_me)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

first_examine = Examine()
first_examine.run()