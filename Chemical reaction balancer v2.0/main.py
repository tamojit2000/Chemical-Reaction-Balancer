# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chemical.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from functions import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Root(object):
    def setupUi(self, Root):
        Root.setObjectName("Root")
        Root.resize(659, 465)
        Root.setMaximumSize(QtCore.QSize(659, 465))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Root.setWindowIcon(icon)
        Root.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(216, 3, 147, 255), stop:0.875 rgba(219, 20, 79, 255));\n"
"padding: 5px;")
        self.centralwidget = QtWidgets.QWidget(Root)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 601, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.History_btn = QtWidgets.QPushButton(self.frame)
        self.History_btn.setGeometry(QtCore.QRect(-50, 120, 100, 100))
        self.History_btn.setStyleSheet("border-radius: 50;\n"
"text-align: right;\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0451977 rgba(59, 255, 27, 255), stop:0.852273 rgba(0, 187, 0, 255));\n"
"padding: 12px;\n"
"")
        self.History_btn.setObjectName("History_btn")
        self.Reset_btn = QtWidgets.QPushButton(self.frame)
        self.Reset_btn.setGeometry(QtCore.QRect(552, 120, 100, 100))
        self.Reset_btn.setStyleSheet("border-radius: 50;\n"
"text-align: left;\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0451977 rgba(59, 255, 27, 255), stop:0.852273 rgba(0, 187, 0, 255));\n"
"padding: 12px;\n"
"")
        self.Reset_btn.setObjectName("Reset_btn")
        self.Balance_btn = QtWidgets.QPushButton(self.frame)
        self.Balance_btn.setGeometry(QtCore.QRect(252, 363, 100, 100))
        self.Balance_btn.setStyleSheet("border-radius: 50;\n"
"text-align: top;\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0451977 rgba(59, 255, 27, 255), stop:0.852273 rgba(0, 187, 0, 255));\n"
"padding: 25px;\n"
"")
        self.Balance_btn.setObjectName("Balance_btn")
        self.Left_entry = QtWidgets.QLineEdit(self.frame)
        self.Left_entry.setGeometry(QtCore.QRect(58, 99, 491, 41))
        self.Left_entry.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
"border-radius: 10px;")
        self.Left_entry.setText("")
        self.Left_entry.setObjectName("Left_entry")
        self.Right_entry = QtWidgets.QLineEdit(self.frame)
        self.Right_entry.setGeometry(QtCore.QRect(58, 201, 491, 41))
        self.Right_entry.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
"border-radius: 10px;")
        self.Right_entry.setObjectName("Right_entry")
        self.Ans_label = QtWidgets.QLabel(self.frame)
        self.Ans_label.setGeometry(QtCore.QRect(58, 305, 491, 41))
        self.Ans_label.setStyleSheet("border: 2px solid rgb(255, 0, 127);\n"
"border-radius: 10px;")
        self.Ans_label.setObjectName("Ans_label")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 156, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(52, 20, 271, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0.0284091, y1:0.034, x2:1, y2:0, stop:0 rgba(255, 0, 173, 255), stop:0.875 rgba(254, 23, 91, 255));")
        self.label_2.setObjectName("label_2")
        Root.setCentralWidget(self.centralwidget)

        self.retranslateUi(Root)
        self.Reset_btn.clicked.connect(self.Left_entry.clear)
        self.Reset_btn.clicked.connect(self.Right_entry.clear)
        self.Reset_btn.clicked.connect(self.Ans_label.clear)
        QtCore.QMetaObject.connectSlotsByName(Root)

        self.History_btn.clicked.connect(History)
        self.Balance_btn.clicked.connect(self.Balance)

    def retranslateUi(self, Root):
        _translate = QtCore.QCoreApplication.translate
        Root.setWindowTitle(_translate("Root", "v 2.0"))
        self.History_btn.setText(_translate("Root", "History"))
        self.Reset_btn.setText(_translate("Root", "Reset"))
        self.Balance_btn.setText(_translate("Root", "Balance"))
        self.Left_entry.setPlaceholderText(_translate("Root", "Enter reactants             eg: H2 + O2"))
        self.Right_entry.setPlaceholderText(_translate("Root", "Enter products             eg: H2O"))
        self.Ans_label.setText(_translate("Root", "Balanced Equation"))
        self.label.setText(_translate("Root", "+"))
        self.label_2.setText(_translate("Root", "Chemical Equation balancer"))


    def Balance(self):
        L=self.Left_entry.text()
        R=self.Right_entry.text()
        if len(L)!=0 and len(R)!=0:
            ans=Calculate(L,R)
            self.Ans_label.setText(ans)
        else:
            self.Ans_label.setText('Please check your entries.')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Root = QtWidgets.QMainWindow()
    ui = Ui_Root()
    ui.setupUi(Root)
    Root.show()
    sys.exit(app.exec_())

