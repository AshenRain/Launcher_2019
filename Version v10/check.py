# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check.ui'
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


class Ui_Form_2(object):
    def setupUi(self, Form_2):
        if Form_2.objectName():
            Form_2.setObjectName(u"Form_2")
        Form_2.resize(400, 179)
        icon = QIcon()
        icon.addFile(u"1234.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form_2.setWindowIcon(icon)
        Form_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(47, 49, 54);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(89, 94, 104);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	font-size: 14px;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"	color: rgb(170, 176, 186);\n"
"}\n"
"	\n"
"QPushButton:hover{\n"
"	background-color: rgb(115, 114, 145);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: silver;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayoutWidget = QWidget(Form_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 90, 341, 62))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.label = QLabel(Form_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 201, 61))
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form_2)

        QMetaObject.connectSlotsByName(Form_2)
    # setupUi

    def retranslateUi(self, Form_2):
        Form_2.setWindowTitle(QCoreApplication.translate("Form_2", u"SC update", None))
        self.pushButton.setText(QCoreApplication.translate("Form_2", u"Update", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form_2", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Form_2", u"New version is found !", None))
    # retranslateUi

