# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yan2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from math import cos, pi, sin

SCREEN_SIZE = [700, 700]
SIDE_LENGTH = 300
SIDES_COUNT = 7
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import csv
from random import randint
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 643)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 560, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 520, 501, 31))
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 180, 501, 301))
        self.listWidget.setObjectName("listWidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 90, 221, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(332, 97, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 490, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(570, 80, 251, 151))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 310, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 310, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 310, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 370, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 370, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(720, 370, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(660, 430, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(600, 430, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(720, 430, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 250, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 500, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 26))
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
        self.pushButton.setText(_translate("MainWindow", "????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????????!"))
        self.label.setText(_translate("MainWindow", "???????? ??????????:"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.label_3.setText(_translate("MainWindow", "??????????????"))
        self.label_4.setText(_translate("MainWindow", "????????????????-????????????"))
        self.label_5.setText(_translate("MainWindow", "???????????????????"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.hide()

        # ???????????? ?????????????? ??????????????????
        self.pushButton_2.clicked.connect(self.run)

        # ???????????? ?????? ???????????????? ???????? ???????????? ???? cvs
        self.vse = []

        #???????????????????? ?????? ?????????????????? ?????????????????? ????????????????
        self.ran = 1
        self.ro = []

        #???????????????????? ???????????????? ??????????
        self.ochki = 0

        #????????
        self.f = True

        #?????? ????????????????????????
        self.name = ''
        self.a = 0
        self.pushButton.clicked.connect(self.otvet)

        with open('vop.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                self.vse.append(row)

        self.pushButton_3.clicked.connect(self.b3)
        self.pushButton_4.clicked.connect(self.b4)
        self.pushButton_5.clicked.connect(self.b5)
        self.pushButton_6.clicked.connect(self.b6)
        self.pushButton_7.clicked.connect(self.b7)
        self.pushButton_8.clicked.connect(self.b8)
        self.pushButton_9.clicked.connect(self.b9)
        self.pushButton_10.clicked.connect(self.b10)
        self.pushButton_11.clicked.connect(self.b11)
        self.count = 0
        self.nol = []
        self.t = 0

    # ?????????????? ???????????????? ?????????????? ?????????????????? ?? ???????????????????? ?????????????????? ?????????????? ??????????????.
    # ???????????????? ???? ???????????? ?????????????????????????? ?????????????????? ?????? ??????????????

    def proverkakrest(self, t):
        while t in self.nol:
            t = randint(3, 11)
            if len(self.nol) == 8:
                break
        if t == 3 and t not in self.nol:
            self.pushButton_3.setText("{}".format('0'))
            self.pushButton_3 = '0'

        elif t == 4 and t not in self.nol:
            self.pushButton_4.setText("{}".format('0'))
            self.pushButton_4 = '0'

        elif t == 11 and t not in self.nol:
            self.pushButton_11.setText("{}".format('0'))
            self.pushButton_11 = '0'

        elif t == 5 and t not in self.nol:
            self.pushButton_5.setText("{}".format('0'))
            self.pushButton_5 = '0'

        elif t == 6 and t not in self.nol:
            self.pushButton_6.setText("{}".format('0'))
            self.pushButton_6 = '0'

        elif t == 7 and t not in self.nol:
            self.pushButton_7.setText("{}".format('0'))
            self.pushButton_7 = '0'

        elif t == 8 and t not in self.nol:
            self.pushButton_8.setText("{}".format('0'))
            self.pushButton_8 = '0'

        elif t == 9 and t not in self.nol:
            self.pushButton_9.setText("{}".format('0'))
            self.pushButton_9 = '0'

        elif t == 10 and t not in self.nol:
            self.pushButton_10.setText("{}".format('0'))
            self.pushButton_10 = '0'

        else:
            self.label_5.setText("{}".format('???????? ????????????????!'))

        self.nol.append(t)

        if self.pushButton_3 == 'X' and self.pushButton_4 == 'X' and self.pushButton_6 == 'X' or \
                self.pushButton_5 == 'X' and self.pushButton_7 == 'X' and self.pushButton_8 == 'X' or \
                self.pushButton_9 == 'X' and self.pushButton_10 == 'X' and self.pushButton_11 == 'X' or \
                self.pushButton_3 == 'X' and self.pushButton_7 == 'X' and self.pushButton_10 == 'X' or \
                self.pushButton_4 == 'X' and self.pushButton_5 == 'X' and self.pushButton_9 == 'X' or \
                self.pushButton_6 == 'X' and self.pushButton_8 == 'X' and self.pushButton_11 == 'X' or \
                self.pushButton_3 == 'X' and self.pushButton_5 == 'X' and self.pushButton_11 == 'X' or \
                self.pushButton_6 == 'X' and self.pushButton_5 == 'X' and self.pushButton_10 == 'X':
            self.label_5.setText("{}".format('?????????????? X'))

        elif self.pushButton_3 == '0' and self.pushButton_4 == '0' and self.pushButton_5 == '0' or \
                self.pushButton_6 == '0' and self.pushButton_7 == '0' and self.pushButton_8 == '0' or \
                self.pushButton_9 == '0' and self.pushButton_10 == '0' and self.pushButton_11 == '0' or \
                self.pushButton_3 == '0' and self.pushButton_7 == '0' and self.pushButton_10 == '0' or \
                self.pushButton_4 == '0' and self.pushButton_5 == '0' and self.pushButton_9 == '0' or \
                self.pushButton_6 == '0' and self.pushButton_8 == '0' and self.pushButton_11 == '0' or \
                self.pushButton_3 == '0' and self.pushButton_5 == '0' and self.pushButton_11 == '0' or \
                self.pushButton_6 == '0' and self.pushButton_5 == '0' and self.pushButton_10 == '0':
            self.label_5.setText("{}".format('?????????????? 0'))

    #?????????????? ???????????? ???????????? ?????????????????????????????? ?????? ???????? ???????????? ??

    def b3(self):
        self.pushButton_3.setText("{}".format('X'))
        self.pushButton_3 = 'X'
        self.count += 1
        self.nol.append(3)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))


    def b4(self):
        self.pushButton_4.setText("{}".format('X'))
        self.pushButton_4 = 'X'
        self.count += 1
        self.nol.append(4)
        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))


    def b5(self):
        self.pushButton_5.setText("{}".format('X'))
        self.pushButton_5 = 'X'
        self.count += 1
        self.nol.append(5)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    def b6(self):
        self.pushButton_6.setText("{}".format('X'))
        self.pushButton_6 = 'X'
        self.count += 1
        self.nol.append(6)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    def b7(self):
        self.pushButton_7.setText("{}".format('X'))
        self.pushButton_7 = 'X'
        self.count += 1
        self.nol.append(7)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    def b8(self):
        self.pushButton_8.setText("{}".format('X'))
        self.pushButton_8 = 'X'
        self.count += 1
        self.nol.append(8)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    def b9(self):
        self.pushButton_9.setText("{}".format('X'))
        self.pushButton_9 = 'X'
        self.count += 1
        self.nol.append(9)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    def b10(self):
        self.pushButton_10.setText("{}".format('X'))
        self.pushButton_10 = 'X'
        self.count += 1
        self.nol.append(10)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    def b11(self):
        self.pushButton_11.setText("{}".format('X'))
        self.pushButton_11 = 'X'
        self.count += 1
        self.nol.append(4)

        if self.count != 8:
            self.count += 1
            t = randint(3, 11)
            self.proverkakrest(t)
        else:
            self.label_5.setText("{}".format('???????? ????????????????'))

    # ?????????????? ?????????????? ?????????????????? ?????? ?????????????????? ???????????????? ?? ?????????? ?????????? ????????????????????????

    def run(self, button):
        self.listWidget.clear()
        self.ochki = 0
        self.f = True
        self.lcdNumber.display(self.ochki)
        self.name, ok_pressed = QInputDialog.getText(self, "?????????????? ??????",
                                                "?????? ???????? ???????????")
        if ok_pressed:
            self.listWidget.addItem(f'????????????, {self.name}! ???????????? ???????? ?????????????????? ???????????????? ???? ?????? ????????????????.\n'
                                    f'???????? ?????????? ?????????????? ?????????????? ???????????? ?? ???????????????? ?????? ?? ???????? ??????????\n'
                                    f'?????????? ??????????!')
            self.label_2.setText(self.name)
        self.ran = randint(1, 12)
        self.ro.append(self.ran)
        self.listWidget.addItem(self.vse[self.ran][1])
        self.pushButton.show()

    # ?????????????? ?????????????? ???? ???????????? "??????????"
    # ???????????????? ???? ???????? ?????????????????? ??????????????

    def otvet(self, button):
        self.pushButton_2.hide()

        if self.textEdit.toPlainText() != 'a' and self.textEdit.toPlainText() != 'b' \
                and self.textEdit.toPlainText() != 'c':
            self.f = False
            self.listWidget.addItem('???????????????? ????????????')

        elif self.textEdit.toPlainText() == self.vse[self.ran][2]:
            self.ochki += 1
            self.lcdNumber.display(self.ochki)
            self.f = True

        else:
            self.f = True

        if self.f:
            self.listWidget.clear()

            while self.ran in self.ro:
                if len(self.ro) == 11:
                    self.ran = 100
                    break
                self.ran = randint(1, 12)

            if self.ran != 100:
                self.ro.append(self.ran)
                self.listWidget.addItem(self.vse[self.ran][1])

            else:
                self.listWidget.addItem('???? ???????? ??????! ?????? ??????? ?????????? ???? ??????????!')
                self.listWidget_2.addItem(f'{self.name} --- {self.ochki}')
                self.pushButton_2.show()
                self.pushButton.hide()
                self.ro = []
                self.ran = 1

    # ???????????????????? ?????????????????????? ?? ???????????????? ????????

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_star(qp)
        qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_star(self, qp):

        # ?????????????? ???????????????????? ?? ?????????????????? ???? ?? ????????????????
        nodes = [(SIDE_LENGTH * cos(i * 2 * pi / SIDES_COUNT),
                  SIDE_LENGTH * sin(i * 2 * pi / SIDES_COUNT))
                 for i in range(SIDES_COUNT)]
        nodes2 = [(int(self.xs(node[0])),
                   int(self.ys(node[1]))) for node in nodes]

        # ???????????? ????????????????????????
        for i in range(-1, len(nodes2) - 1):
            qp.drawLine(*nodes2[i], *nodes2[i + 1])

        # ???????????????? ???????? ??????????
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)

        # ???????????? ????????????
        for i in range(-2, len(nodes2) - 2):
            qp.drawLine(*nodes2[i], *nodes2[i + 2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())