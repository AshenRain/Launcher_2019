# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(637, 438)
        Dialog.setMinimumSize(QSize(637, 438))
        Dialog.setMaximumSize(QSize(637, 438))
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color:rgb(106, 106, 106);\n"
"	background-image: url(com_11.jpg);\n"
"	background-position: midle;\n"
"}\n"
"\n"
"QPushButton{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(77, 80, 102);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(165, 166, 182);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"	\n"
"QPushButton:hover{\n"
"	background-color: rgb(115, 114, 145);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: silver;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	width: 75px;\n"
"	height"
                        ": 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(165, 166, 182);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 370, 141, 51))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 370, 141, 51))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 60, 161, 41))
        self.hboxLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.hboxLayout.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"text-color white;")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.hboxLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 381, 21))
        self.horizontalLayoutWidget_2 = QWidget(Dialog)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(400, 10, 221, 62))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 140, 341, 201))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(19, 110, 300, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"SC Legacy", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Play", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Check update", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"None", None))
        self.lineEdit.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Find SCFA", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        #self.label_3.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "https://ru.stackoverflow.com/", None))
    # retranslateUi

