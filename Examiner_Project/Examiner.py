#Examiner
#--------


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading
import time
import Database


class Examine:

    def __init__(self):
        self.time = ''

    def return_spanish_word(self):

        spanish_word = Database.return_words()[0]

        return spanish_word

class Vocabulary:

    def __init__(self):

        self.english = ''
        self.spanish = ''

    def add_word(self):

        self.spanish = input('Write spanish meaning: ')
        self.english = input('Write english menaing: ')

        Database.insert_value(self.spanish, self.english)

class Score:

    def __init__(self):

        self.score = 0

    def increase_score(self):

        if self.score < 0:
            self.score = 0
        else:
            self.score += 1

    def decrease_score(self):

        self.score -=1

    def show_score(self):

        return self.score


score_object = Score()


examine_object = Examine()
#first_examine.examine_me()
examine_object.return_spanish_word()

#add_vocab = Vocabulary()

#add_vocab.add_word()
#add_vocab.check_vocabulary()
#add_vocab.add_word()

#Database.insert_value("dos", "two")


