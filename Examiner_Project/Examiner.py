#Examiner
#--------



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading
import time, random

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

        self.new_word = []

    def add_word(self):

        self.new_word.append(input('Write spanish meaning'))
        self.new_word.append(input('Write english menaing'))

        vocabulary.append(self.new_word)
        print(f'The word {self.new_word} was added')

    def check_vocabulary(self):

        return vocabulary


#first_examine = Examine()
#first_examine.run()

add_vocab = Vocabulary()

add_vocab.add_word()
print(add_vocab.check_vocabulary())