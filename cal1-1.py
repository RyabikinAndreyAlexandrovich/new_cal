#version 1.2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from math import *


def res(self):
    try:
        fir = float(self.label_1.text())
        sec = self.label_2.text()
        if sec == '!':
            self.label_4.setText("={}".format(factorial(fir)))
            return
        if sec == '√' and fir >= 0:
            self.label_4.setText("={}".format(sqrt(fir)))
            return
        thi = float(self.label_3.text())
        if sec == '*':
            self.label_4.setText("={}".format(fir * thi))
        if sec == '**':
            self.label_4.setText("={}".format(fir ** thi))
        if sec == '/':
            self.label_4.setText("={}".format(fir / thi))
        if sec == '-':
            self.label_4.setText("={}".format(fir - thi))
        if sec == '+':
            self.label_4.setText("={}".format(fir + thi))
    except Exception:
        self.label_4.setText("ERROR")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 326, 328))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.button8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.button8)
        self.button9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.button9)
        self.button6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button6)
        self.button7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.button7)
        self.button4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.button4)
        self.button5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.button5)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.button2)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.button3)
        self.button0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.button0)
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.button1)
        self.buttonPoint = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonPoint.setFont(font)
        self.buttonPoint.setObjectName("buttonPoint")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.buttonPoint)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.buttonC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonC.setFont(font)
        self.buttonC.setObjectName("buttonC")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.buttonC)
        self.buttonDEL = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonDEL.setFont(font)
        self.buttonDEL.setObjectName("buttonDEL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.buttonDEL)
        self.buttonStepen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStepen.sizePolicy().hasHeightForWidth())
        self.buttonStepen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonStepen.setFont(font)
        self.buttonStepen.setObjectName("buttonStepen")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.buttonStepen)
        self.buttonRovno = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonRovno.setFont(font)
        self.buttonRovno.setObjectName("buttonRovno")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonRovno)
        self.buttonPlus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonPlus.setFont(font)
        self.buttonPlus.setObjectName("buttonPlus")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.buttonPlus)
        self.buttonMinus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonMinus.setFont(font)
        self.buttonMinus.setObjectName("buttonMinus")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonMinus)
        self.buttonFactor = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonFactor.setFont(font)
        self.buttonFactor.setObjectName("buttonFactor")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.buttonFactor)
        self.buttonKoren = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonKoren.setFont(font)
        self.buttonKoren.setObjectName("buttonKoren")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonKoren)
        self.buttonMulti = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonMulti.setFont(font)
        self.buttonMulti.setObjectName("buttonMulti")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.buttonMulti)
        self.buttonDelenie = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonDelenie.setFont(font)
        self.buttonDelenie.setObjectName("buttonDelenie")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonDelenie)
        self.buttonChange = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonChange.setFont(font)
        self.buttonChange.setObjectName("buttonChange")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.buttonChange)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.verticalLayout.addLayout(self.formLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.buttonPoint.setText(_translate("MainWindow", "."))
        self.buttonC.setText(_translate("MainWindow", "C"))
        self.buttonDEL.setText(_translate("MainWindow", "←"))
        self.buttonStepen.setText(_translate("MainWindow", "**"))
        self.buttonRovno.setText(_translate("MainWindow", "="))
        self.buttonPlus.setText(_translate("MainWindow", "+"))
        self.buttonMinus.setText(_translate("MainWindow", "-"))
        self.buttonFactor.setText(_translate("MainWindow", "!"))
        self.buttonKoren.setText(_translate("MainWindow", "√"))
        self.buttonMulti.setText(_translate("MainWindow", "*"))
        self.buttonDelenie.setText(_translate("MainWindow", "/"))
        self.buttonChange.setText(_translate("MainWindow", "+/-"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button0.clicked.connect(self.run_0)
        self.button1.clicked.connect(self.run_1)
        self.button2.clicked.connect(self.run_2)
        self.button3.clicked.connect(self.run_3)
        self.button4.clicked.connect(self.run_4)
        self.button5.clicked.connect(self.run_5)
        self.button6.clicked.connect(self.run_6)
        self.button7.clicked.connect(self.run_7)
        self.button8.clicked.connect(self.run_8)
        self.button9.clicked.connect(self.run_9)
        self.buttonC.clicked.connect(self.run_c)
        self.buttonDEL.clicked.connect(self.run_del)
        self.buttonMulti.clicked.connect(self.run_multi)
        self.buttonMinus.clicked.connect(self.run_minus)
        self.buttonPlus.clicked.connect(self.run_plus)
        self.buttonStepen.clicked.connect(self.run_stepen)
        self.buttonKoren.clicked.connect(self.run_koren)
        self.buttonFactor.clicked.connect(self.run_factor)
        self.buttonDelenie.clicked.connect(self.run_delenie)
        self.buttonRovno.clicked.connect(self.run_rovno)
        self.buttonPoint.clicked.connect(self.run_point)
        self.buttonChange.clicked.connect(self.run_change)

    def run_0(self):
        if self.label_2.text() == '' and self.label_1.text() != '0':
            self.label_1.setText("{}".format(str(self.label_1.text() + '0')))
        if self.label_2.text() != '' and self.label_3.text() != '0':
            self.label_3.setText("{}".format(str(self.label_3.text() + '0')))
            res(self)

    def run_1(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '1')))
            else:
                self.label_1.setText('1')
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '1')))
            else:
                self.label_3.setText('1')
            res(self)

    def run_2(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '2')))
            else:
                self.label_1.setText("2")
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '2')))
            else:
                self.label_3.setText("2")
            res(self)

    def run_3(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '3')))
            else:
                self.label_1.setText("3")
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '3')))
            else:
                self.label_3.setText("3")
            res(self)

    def run_4(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '4')))
            else:
                self.label_1.setText("4")
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '4')))
            else:
                self.label_3.setText("4")
            res(self)

    def run_5(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '5')))
            else:
                self.label_1.setText("5")
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '5')))
            else:
                self.label_3.setText("5")
            res(self)

    def run_6(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '6')))
            else:
                self.label_1.setText('6')
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '6')))
            else:
                self.label_3.setText('6')
            res(self)

    def run_7(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '7')))
            else:
                self.label_1.setText('7')
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '7')))
            else:
                self.label_3.setText('7')
            res(self)

    def run_8(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '8')))
            else:
                self.label_1.setText('8')
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '8')))
            else:
                self.label_3.setText('8')
            res(self)

    def run_9(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(str(self.label_1.text() + '9')))
            else:
                self.label_1.setText('9')
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '0':
                self.label_3.setText("{}".format(str(self.label_3.text() + '9')))
            else:
                self.label_3.setText('9')
            res(self)

    def run_c(self):
        self.label_1.setText('')
        self.label_2.setText('')
        self.label_3.setText('')
        self.label_4.setText('')

    def run_del(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '':
                self.label_1.setText("{}".format(self.label_1.text()[:-1]))
        if self.label_2.text() != '' and self.label_3.text() == '':
            self.label_2.setText('')
            self.label_4.setText('')
        if self.label_2.text() != '' and self.label_3.text() != '':
            self.label_3.setText("{}".format(self.label_3.text()[:-1]))
            if self.label_3.text() == '-':
                self.label_3.setText('')
                self.label_4.setText('')
            else:
                res(self)

    def run_multi(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('*')

    def run_minus(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('-')

    def run_plus(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('+')

    def run_stepen(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('**')

    def run_koren(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('√')
            res(self)

    def run_factor(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('!')
            res(self)

    def run_delenie(self):
        if self.label_1.text() != '':
            if self.label_4.text() != '':
                self.run_rovno()
            self.label_2.setText('/')

    def run_rovno(self):
        if self.label_4.text() != 'ERROR' and self.label_4.text() != "":
            self.label_1.setText("{}".format(self.label_4.text()[1::]))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")

    def run_point(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '' and '.' not in self.label_1.text():
                self.label_1.setText("{}".format(str(self.label_1.text() + '.')))
            if self.label_1.text() == '':
                self.label_1.setText('0.')
        if self.label_2.text() not in ['', '!', '√']:
            if self.label_3.text() != '' and '.' not in self.label_3.text():
                self.label_3.setText("{}".format(str(self.label_3.text() + '.')))
            if self.label_3.text() == '':
                self.label_3.setText('0.')

    def run_change(self):
        if self.label_2.text() == '':
            if self.label_1.text() != '0':
                self.label_1.setText("{}".format(-float(self.label_1.text())))
        if self.label_3.text() not in ['', '0']:
            self.label_3.setText("{}".format(-float(self.label_3.text())))
            res(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
