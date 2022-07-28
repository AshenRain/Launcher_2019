# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Empty\Desktop\Launcher SCFA\Version v5\launcher.ui'
#
# Created: Wed Mar 25 19:14:51 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 438)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:rgb(106, 106, 106);\n"
"	 background-image: url(com_11.jpg);\n"
"	 background-position: midle;\n"
"}\n"
"\n"
"QPushButton{\n"
"    float: right;\n"
"    border-radius: 5px;\n"
"    padding: 5px 9px;\n"
"    font-size: 1.2em;\n"
"    background-color: rgb(77, 80, 102);\n"
"    border-bottom: 4px solid rgba(217,91,72,1);\n"
"    color: white;\n"
"    font-family: \'Roboto Slab\', serif;\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"    float: right;\n"
"    border-radius: 5px;\n"
"    padding: 5px 9px;\n"
"    font-size: 1.2em;\n"
"    background-color: rgb(165, 166, 182);\n"
"    border-bottom: 4px solid rgba(217,91,72,1);\n"
"    color: white;\n"
"    font-family: \'Roboto Slab\', serif;\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"    \n"
"QPushButton:hover{\n"
"    background-color: rgb(115, 114, 145);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    float: right;\n"
"    border-radius: 5px;\n"
"    padding: 5px 9px;\n"
"    font-size: 1.2em;\n"
"    background-color: rgb(165, 166, 182);\n"
"    border-bottom: 4px solid rgba(217,91,72,1);\n"
"    color: white;\n"
"    font-family: \'Roboto Slab\', serif;\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(480, 370, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 370, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 161, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hboxlayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("color white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("text-color white;")
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 10, 221, 62))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 140, 341, 201))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "SC Legacy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Check update", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Find SCFA", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Confirm", None, QtGui.QApplication.UnicodeUTF8))




