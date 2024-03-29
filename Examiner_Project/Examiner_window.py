# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Examiner_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Examiner, Database
import PyQt5
from Examiner import Score


class Ui_MainWindow(object):

    def __init__(self):

        self.num_of_translations = 0

        self.good_translations = ''
        self.wrong_translations = ''


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Start = QtWidgets.QPushButton(self.centralwidget) # start button, starts examination
        self.Start.setGeometry(QtCore.QRect(60, 120, 93, 28))
        self.Start.setObjectName("Start")

        self.insert_meaning = QtWidgets.QPushButton(self.centralwidget) # insert meaning button to database
        self.insert_meaning.setGeometry(QtCore.QRect(200, 350, 93, 28))
        self.insert_meaning.setObjectName("Insert meaning")

        self.translate_to_eng_label = QtWidgets.QLabel(self.centralwidget) # label translate to english
        self.translate_to_eng_label.setGeometry(QtCore.QRect(60, 160, 131, 31))
        self.translate_to_eng_label.setObjectName("label1")

        self.user_translation = QtWidgets.QLineEdit(self.centralwidget) # translation from the user
        self.user_translation.setGeometry(QtCore.QRect(310, 160, 113, 22))
        self.user_translation.setObjectName("user_translation")

        self.insert_spanish_edit = QtWidgets.QLineEdit(self.centralwidget) # spanish word input to database
        self.insert_spanish_edit.setGeometry(QtCore.QRect(400, 430, 113, 22))
        self.insert_spanish_edit.setObjectName("user_translation")

        self.insert_english_edit = QtWidgets.QLineEdit(self.centralwidget) # english word input to database
        self.insert_english_edit.setGeometry(QtCore.QRect(200, 430, 113, 22))
        self.insert_english_edit.setObjectName("user_translation")

        self.spanish_word = QtWidgets.QLabel(self.centralwidget) # spanish word to database label
        self.spanish_word.setGeometry(QtCore.QRect(200, 168, 90, 20))
        self.spanish_word.setObjectName("spanish_word")

        self.insert_english = QtWidgets.QLabel(self.centralwidget) # english word to database label
        self.insert_english.setGeometry(QtCore.QRect(200, 400, 150, 20))
        self.insert_english.setObjectName("insert_english")

        self.insert_spanish = QtWidgets.QLabel(self.centralwidget) # spanish word to database label
        self.insert_spanish.setGeometry(QtCore.QRect(400, 400, 150, 20))
        self.insert_spanish.setObjectName("insert_spanish")

        self.english_word = QtWidgets.QLabel(self.centralwidget) # right translation for developing purposes
        self.english_word.setGeometry(QtCore.QRect(200, 220, 90, 20))
        self.english_word.setObjectName("english_word")

        self.right_translation = QtWidgets.QLabel(self.centralwidget) # shows "right translation was" when translated incorrectly
        self.right_translation.setGeometry(QtCore.QRect(480, 168, 100, 16))
        self.right_translation.setObjectName("right_translation")

        self.check_of_translation = QtWidgets.QLabel(self.centralwidget) # displays "wrong translation" or "good translation"
        self.check_of_translation.setGeometry(QtCore.QRect(310, 130, 55, 16))
        self.check_of_translation.setObjectName("check_of_translation")

        self.score = QtWidgets.QLabel(self.centralwidget) # shows score of the user
        self.score.setGeometry(QtCore.QRect(60, 230, 55, 16))
        self.score.setObjectName("score")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.right_translation.setHidden(True)
        self.english_word.setHidden(False) # right translation displayed in window as a check

        self.Start.clicked.connect(self.show_spanish_word)
        self.Start.clicked.connect(self.show_english_translation_check)

        self.insert_meaning.clicked.connect(self.new_database_item) # adds item in database


        self.user_translation.returnPressed.connect(lambda: self.check_the_translation())
        self.user_translation.returnPressed.connect(lambda: self.show_english_translation_check()) # showing the right translation for dev purpose



        if self.num_of_translations == 2:

            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setText("Hello")
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Examiner"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.insert_meaning.setText(_translate("MainWindow", "Insert meaning"))
        self.score.setText(_translate("MainWindow", "Your score is:"))
        self.translate_to_eng_label.setText(_translate("MainWindow", "Translate to english:"))
        self.spanish_word.setText(_translate("MainWindow", "spanish_word"))
        self.english_word.setText(_translate("MainWindow", "english_word"))
        self.check_of_translation.setText(_translate("MainWindow", "Evaluation"))
        self.right_translation.setText(_translate("MainWindow", "Right translation was"))
        self.insert_english.setText(_translate("MainWindow", "English meaning"))
        self.insert_spanish.setText(_translate("MainWindow", "Spanish meaning"))

    def check_the_translation(self): # checks the translation and evaluates score

        print(self.num_of_translations)


        if self.spanish_word.text() == Database.english_in_spanish_out(self.user_translation.text()):
            self.right_translation.setHidden(True)
            self.check_of_translation.setText("Right translation ")
            self.check_of_translation.setStyleSheet("color:green")
            self.check_of_translation.adjustSize()
            Examiner.score_object.increase_score()
            self.score.setText("Your score is " + str(Examiner.score_object.show_score()))

            self.good_translations += self.spanish_word.text() + " - " + self.user_translation.text() + ", "
        else:
            self.check_of_translation.setText("Wrong translation ")
            self.check_of_translation.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold)) #set the font to bold
            self.check_of_translation.setStyleSheet("color:red")
            self.check_of_translation.adjustSize()
            self.right_translation.setHidden(False)
            self.right_translation_word = Database.spanish_in_english_out(self.spanish_word.text())
            self.right_translation.setText("Righ translation was: " + self.right_translation_word +
                                           " ... you put: " + self.user_translation.text() )
            self.right_translation.adjustSize()
            Examiner.score_object.decrease_score()
            self.score.setText("Your score is " + str(Examiner.score_object.show_score()))

            self.wrong_translations += self.spanish_word.text() + " - " + self.user_translation.text() + ", "

        self.score.adjustSize()
        self.user_translation.clear()
        self.show_spanish_word()

        Ui_MainWindow.count_translations_evaluation(self)

    def count_translations_evaluation(self): # evaluation button after examination round

        self.num_of_translations += 1

        if self.num_of_translations == 3:

            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setText("Traslation round evaluation")
            msg.setWindowTitle("Evaluation")
            print(self.wrong_translations)
            msg.setDetailedText("Right translated was: " + str(self.good_translations) + "\n" +
                                "Wrong translated was: " + str(self.wrong_translations))
            msg.setStyleSheet("QLabel{min-width: 500px;}")

            msg.exec_()
            self.num_of_translations = 0

    def new_database_item(self): # inserts words in examiner database

        if not ( self.insert_english_edit.text() and self.insert_spanish_edit.text() ):

            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setText("There are no input words, please insert them")
            msg.exec_()

        else:

            spanish = self.insert_spanish_edit.text()
            english = self.insert_english_edit.text()

            qm = PyQt5.QtWidgets.QMessageBox()
            rep = qm.question(self.centralwidget, '', 'Are you sure you want to insert the words?', qm.Yes | qm.No)
            if rep == qm.Yes:
                Database.insert_value(spanish, english)
                confirm_msg = PyQt5.QtWidgets.QMessageBox()
                confirm_msg.setText(f'The spanish word {spanish} with translation {english} was added.')
                confirm_msg.exec_()


            else:
                print (" Will not add words")
           # Database.insert_value(spanish,english)

        self.insert_spanish_edit.clear()
        self.insert_english_edit.clear()


    def show_spanish_word(self):
        self.spanish_word.setText(Examiner.examine_object.return_spanish_word())
        self.update_label_spanish_word()


    def update_label_spanish_word(self):
        self.spanish_word.adjustSize()

    def update_label_english_word(self):
        self.english_word.adjustSize()

    def show_english_translation_check(self): # returns english translation to check the right translated state
        self.english_word.setText(Database.spanish_in_english_out(self.spanish_word.text()))
        self.update_label_english_word()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())







