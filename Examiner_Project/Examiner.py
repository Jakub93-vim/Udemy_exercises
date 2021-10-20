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

    def check_vocabulary(self):

        return Database.show_vocabulary()


examine_object = Examine()
#first_examine.examine_me()
examine_object.return_spanish_word()
vocabulary = Vocabulary()
#vocabulary.check_vocabulary()
#vocabulary.add_word()


#add_vocab = Vocabulary()

#add_vocab.add_word()
#add_vocab.check_vocabulary()
#add_vocab.add_word()

#Database.insert_value("dos", "two")


