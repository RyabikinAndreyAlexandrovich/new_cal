#Version 1.4 with keyboard input, but without lots of functions
#Some bugs have been fixed and the program termination feature has been added
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
        MainWindow.resize(298, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(50, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(90, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(50, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.buttonKoren = QtWidgets.QPushButton(self.centralwidget)
        self.buttonKoren.setGeometry(QtCore.QRect(250, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonKoren.setFont(font)
        self.buttonKoren.setObjectName("buttonKoren")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(50, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.buttonSin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSin.setGeometry(QtCore.QRect(210, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonSin.setFont(font)
        self.buttonSin.setObjectName("buttonSin")
        self.buttonChange = QtWidgets.QPushButton(self.centralwidget)
        self.buttonChange.setGeometry(QtCore.QRect(90, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonChange.setFont(font)
        self.buttonChange.setObjectName("buttonChange")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(10, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.buttonMulti = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMulti.setGeometry(QtCore.QRect(170, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonMulti.setFont(font)
        self.buttonMulti.setObjectName("buttonMulti")
        self.buttonStepen = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStepen.setGeometry(QtCore.QRect(250, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonStepen.setFont(font)
        self.buttonStepen.setObjectName("buttonStepen")
        self.buttonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlus.setGeometry(QtCore.QRect(170, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonPlus.setFont(font)
        self.buttonPlus.setObjectName("buttonPlus")
        self.buttonRovno = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRovno.setGeometry(QtCore.QRect(170, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonRovno.setFont(font)
        self.buttonRovno.setObjectName("buttonRovno")
        self.buttonTg = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTg.setGeometry(QtCore.QRect(210, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonTg.setFont(font)
        self.buttonTg.setObjectName("buttonTg")
        self.buttonCos = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCos.setGeometry(QtCore.QRect(250, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonCos.setFont(font)
        self.buttonCos.setObjectName("buttonCos")
        self.buttonDelenie = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDelenie.setGeometry(QtCore.QRect(210, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonDelenie.setFont(font)
        self.buttonDelenie.setObjectName("buttonDelenie")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(10, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.buttonFactor = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFactor.setGeometry(QtCore.QRect(170, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonFactor.setFont(font)
        self.buttonFactor.setObjectName("buttonFactor")
        self.buttonMinus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMinus.setGeometry(QtCore.QRect(210, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonMinus.setFont(font)
        self.buttonMinus.setObjectName("buttonMinus")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(90, 160, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(90, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 240, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.buttonCtg = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCtg.setGeometry(QtCore.QRect(250, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonCtg.setFont(font)
        self.buttonCtg.setObjectName("buttonCtg")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(50, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.buttonDEL = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDEL.setGeometry(QtCore.QRect(90, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonDEL.setFont(font)
        self.buttonDEL.setObjectName("buttonDEL")
        self.buttonC = QtWidgets.QPushButton(self.centralwidget)
        self.buttonC.setGeometry(QtCore.QRect(50, 110, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonC.setFont(font)
        self.buttonC.setObjectName("buttonC")
        self.buttonPoint = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPoint.setGeometry(QtCore.QRect(10, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonPoint.setFont(font)
        self.buttonPoint.setObjectName("buttonPoint")
        self.buttonPi = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPi.setGeometry(QtCore.QRect(170, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonPi.setFont(font)
        self.buttonPi.setObjectName("buttonPi")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1= QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setText("")
        self.label_1.setObjectName("label")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 298, 21))
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
        self.button0.setText(_translate("MainWindow", "0"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.buttonKoren.setText(_translate("MainWindow", "√"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.buttonSin.setText(_translate("MainWindow", "sin()"))
        self.buttonChange.setText(_translate("MainWindow", "+/-"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.buttonMulti.setText(_translate("MainWindow", "*"))
        self.buttonStepen.setText(_translate("MainWindow", "**"))
        self.buttonPlus.setText(_translate("MainWindow", "+"))
        self.buttonRovno.setText(_translate("MainWindow", "="))
        self.buttonTg.setText(_translate("MainWindow", "tg()"))
        self.buttonCos.setText(_translate("MainWindow", "cos()"))
        self.buttonDelenie.setText(_translate("MainWindow", "/"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.buttonFactor.setText(_translate("MainWindow", "!"))
        self.buttonMinus.setText(_translate("MainWindow", "-"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.buttonCtg.setText(_translate("MainWindow", "ctg()"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.buttonDEL.setText(_translate("MainWindow", "←"))
        self.buttonC.setText(_translate("MainWindow", "C"))
        self.buttonPoint.setText(_translate("MainWindow", "."))
        self.buttonPi.setText(_translate("MainWindow", "¶"))


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

    def keyPressEvent(self, event):
        if event.key() == 48:
            self.run_0()
        if event.key() == 49:
            self.run_1()
        if event.key() == 50:
            self.run_2()
        if event.key() == 51:
            self.run_3()
        if event.key() == 52:
            self.run_4()
        if event.key() == 53:
            self.run_5()
        if event.key() == 54:
            self.run_6()
        if event.key() == 55:
            self.run_7()
        if event.key() == 56:
            self.run_8()
        if event.key() == 57:
            self.run_9()
        if event.key() == 16777219:
            self.run_del()
        if event.key() == 16777220 or event.key() == 16777221:
            self.run_rovno()
        if event.key() == 46:
            self.run_point()
        if event.key() == 47:
            self.run_delenie()
        if event.key() == 42:
            self.run_multi()
        if event.key() == 61:
            self.run_rovno()
        if event.key() == 45:
            self.run_minus()
        if event.key() == 43:
            self.run_plus()
        if event.key() == 16777216:
            self.close()

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
