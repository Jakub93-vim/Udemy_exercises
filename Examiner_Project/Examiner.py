#Examiner
#--------



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading
import time, random
import Database

vocabulary = [['que','that'],['para','for'],['aquí','here'],['caballo','horse'],
              ['madera','wood'],['carta','letter'],['canción','song']]

class Examine:

    def __init__(self):
        self.time = ''


    def countdown(self):
        t = 5
        while t > 0:
            print("\r", 'Remaining time:', t, end="")
            t -= 1
            time.sleep(1)
        print("\r", 'Time ended', end="")

    def examine_me(self):

        rand_int = random.randint(0,len(vocabulary)-1)
        check = input(f'Translate {vocabulary[rand_int][0]} to english: ')


        if check == vocabulary[rand_int][1]:
            print("You are right !")
        else:
            print(f"No, the translation is: {vocabulary[rand_int][1]}")


    def run(self):

        t1 = threading.Thread(target=self.countdown)
        t2 = threading.Thread(target=self.examine_me)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

class Vocabulary:

    def __init__(self):

        self.english = ''
        self.spanish = ''

    def add_word(self):

        self.spanish = input('Write spanish meaning: ')
        self.english = input('Write english menaing: ')

        Database.insert_value(self.spanish, self.english)

    def check_vocabulary(self):

        return Database.show_vocabulary()


#first_examine = Examine()
#first_examine.run()

add_vocab = Vocabulary()

#add_vocab.add_word()
add_vocab.check_vocabulary()
#add_vocab.add_word()

#Database.insert_value("dos", "two")
