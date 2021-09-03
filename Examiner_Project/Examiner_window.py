# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Examiner_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Examiner, Database


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Test_me = QtWidgets.QPushButton(self.centralwidget)
        self.Test_me.setGeometry(QtCore.QRect(60, 120, 93, 28))
        self.Test_me.setObjectName("Test_me")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(60, 160, 131, 31))
        self.label1.setObjectName("label1")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 160, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.spanish_word = QtWidgets.QLabel(self.centralwidget)
        self.spanish_word.setGeometry(QtCore.QRect(200, 170, 55, 16))
        self.spanish_word.setObjectName("spanish_word")

        self.right_translation = QtWidgets.QLabel(self.centralwidget)
        self.right_translation.setGeometry(QtCore.QRect(480, 170, 100, 16))
        self.right_translation.setObjectName("right_translation")

        self.check_of_translation = QtWidgets.QLabel(self.centralwidget)
        self.check_of_translation.setGeometry(QtCore.QRect(320, 130, 55, 16))
        self.check_of_translation.setObjectName("check_of_translation")

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

        self.Test_me.clicked.connect(self.show_spanish_word)

        self.lineEdit.returnPressed.connect(lambda: self.check_the_translation())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Examiner"))
        self.Test_me.setText(_translate("MainWindow", "Test me !"))
        self.label1.setText(_translate("MainWindow", "Translate to english:"))
        self.spanish_word.setText(_translate("MainWindow", "TextLabel"))
        self.check_of_translation.setText(_translate("MainWindow", "Evaluation"))
        self.right_translation.setText(_translate("MainWindow", "Right translation was"))

    def check_the_translation(self):

        #print (self.spanish_word.text())
        #print(Database.verify_translation(self.lineEdit.text()))
        #english_translation = Database.english_in_spanish_out(self.lineEdit.text())
        try:
            if self.spanish_word.text() == Database.english_in_spanish_out(self.lineEdit.text()):
                self.check_of_translation.setText("Right translation ")
                self.check_of_translation.adjustSize()
            else:
                self.check_of_translation.setText("Wrong translation ")
                self.check_of_translation.adjustSize()
                self.right_translation.setHidden(False)
                self.right_translation.setText("Righ translation was", Database.english_in_spanish_out(self.lineEdit.text()) )
            #print (Database.verify_translation(to_verify))
        except:
            self.check_of_translation.setText("Wrong translation ")
            self.right_translation.adjustSize()
            self.right_translation.setHidden(False)
            self.right_translation.setText("Righ translation was", Database.english_in_spanish_out("we"))

        self.show_spanish_word()


    def show_spanish_word(self):
        self.spanish_word.setText(Examiner.examine_object.return_spanish_word())
        self.update_label_spanish_word()


    def update_label_spanish_word(self):
        self.spanish_word.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






