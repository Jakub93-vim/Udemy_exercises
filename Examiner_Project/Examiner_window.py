# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Examiner_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Examiner, Database
import PyQt5
from Examiner import Score


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(60, 120, 93, 28))
        self.Start.setObjectName("Start")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(60, 160, 131, 31))
        self.label1.setObjectName("label1")

        self.user_translation = QtWidgets.QLineEdit(self.centralwidget)
        self.user_translation.setGeometry(QtCore.QRect(310, 160, 113, 22))
        self.user_translation.setObjectName("user_translation")

        self.spanish_word = QtWidgets.QLabel(self.centralwidget)
        self.spanish_word.setGeometry(QtCore.QRect(200, 168, 90, 20))
        self.spanish_word.setObjectName("spanish_word")

        self.english_word = QtWidgets.QLabel(self.centralwidget)
        self.english_word.setGeometry(QtCore.QRect(200, 220, 90, 20))
        self.english_word.setObjectName("english_word")

        self.right_translation = QtWidgets.QLabel(self.centralwidget)
        self.right_translation.setGeometry(QtCore.QRect(480, 168, 100, 16))
        self.right_translation.setObjectName("right_translation")

        self.check_of_translation = QtWidgets.QLabel(self.centralwidget)
        self.check_of_translation.setGeometry(QtCore.QRect(310, 130, 55, 16))
        self.check_of_translation.setObjectName("check_of_translation")

        self.score = QtWidgets.QLabel(self.centralwidget)
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

        for i in (0,5):
            self.user_translation.returnPressed.connect(lambda: self.check_the_translation())
            self.user_translation.returnPressed.connect(lambda: self.show_english_translation_check())
            i += 1

            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setText("Hello")
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Examiner"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.score.setText(_translate("MainWindow", "Your score is:"))
        self.label1.setText(_translate("MainWindow", "Translate to english:"))
        self.spanish_word.setText(_translate("MainWindow", "spanish_word"))
        self.english_word.setText(_translate("MainWindow", "english_word"))
        self.check_of_translation.setText(_translate("MainWindow", "Evaluation"))
        self.right_translation.setText(_translate("MainWindow", "Right translation was"))

    def check_the_translation(self):

        self.right_translation.setHidden(True)

        if self.spanish_word.text() == Database.english_in_spanish_out(self.user_translation.text()):
            self.check_of_translation.setText("Right translation ")
            self.check_of_translation.setStyleSheet("color:green")
            self.check_of_translation.adjustSize()
            Examiner.score_object.increase_score()
            self.score.setText("Your score is " + str(Examiner.score_object.show_score()))
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

        self.score.adjustSize()
        self.user_translation.clear()
        self.show_spanish_word()


    def show_spanish_word(self):
        self.spanish_word.setText(Examiner.examine_object.return_spanish_word())
        self.update_label_spanish_word()


    def update_label_spanish_word(self):
        self.spanish_word.adjustSize()

    def update_label_english_word(self):
        self.english_word.adjustSize()

    def show_english_translation_check(self):
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







