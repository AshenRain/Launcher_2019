# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher_2.ui'
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
        Dialog.resize(608, 274)
        Dialog.setMinimumSize(QSize(608, 274))
        Dialog.setMaximumSize(QSize(608, 274))
        Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"1234.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color:rgb(54, 57, 63);\n"
"}\n"
"\"rgb(142, 146, 151)  text\"\n"
"\"rgb(47, 49, 54) back\"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QTabWidget\n"
" {\n"
"     border-top: 1px solid gray;\n"
"     border-left: 1px solid gray;\n"
"     border-right: 1px solid gray;\n"
"     border-bottom: 1px solid gray;\n"
" }\n"
"\n"
"\n"
"\n"
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
"	height: 5"
                        "0px;\n"
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
"	height: 50px;\n"
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
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-10, 0, 651, 451))
        self.tabWidget.setMinimumSize(QSize(651, 0))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
" {\n"
"     border-top: rgb(47, 49, 54);\n"
"     border-left: 1px solid gray;\n"
"     border-right: 1px solid gray;\n"
"     border-bottom: 1px solid gray;\n"
" }\n"
"\n"
" QTabBar::tab\n"
" {\n"
"    \n"
"	float: right;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(89, 94, 104);\n"
"	border-bottom: rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"     min-width: 320px;\n"
"     padding-top : 6px;\n"
"     padding-bottom : 8px;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"	color: rgb(170, 176, 186);\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover \n"
"{\n"
"     background-color: rgb(77, 80, 102);\n"
" }\n"
"\n"
"QPushButton{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(89, 94, 104);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
""
                        "	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"	color: rgb(170, 176, 186);\n"
"\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	float: right;\n"
"	border-radius: 5px;\n"
"	padding: 5px 9px;\n"
"	font-size: 1.2em;\n"
"	background-color: rgb(104, 110, 121);\n"
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
"	background-color: rgb(77, 80, 102);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: silver;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(170, 176, 186);\n"
"	width: 75px;\n"
"	height: 50px;\n"
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
"	background-color: rgb(104, 110, 121);\n"
"	border-bottom: 4px solid rgba(217,91,72,1);\n"
"	color: white;"
                        "\n"
"	font-family: 'Roboto Slab', serif;\n"
"	width: 75px;\n"
"	height: 50px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFocusPolicy(Qt.TabFocus)
        self.tab.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 210, 181, 31))
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 170, 181, 31))
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(430, 10, 181, 31))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(430, 50, 181, 31))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 10, 391, 21))
        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 100, 391, 141))
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 194, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 121, 20))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(430, 10, 181, 31))
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 40, 391, 21))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 121, 16))
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 110, 391, 21))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 151, 16))
        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(290, 70, 121, 23))
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(290, 140, 121, 23))
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(430, 170, 181, 31))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 140, 151, 20))
        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(430, 210, 181, 31))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"SCLegacy", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Play                                  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Check update                 ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Find SCFA                       ", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Confirm                           ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"None", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Main", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Delete Version               ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"ID file on server", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"ID version on server", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"2.6.4", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Install stable version", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"67 (Tournament)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Settings", None))
    # retranslateUi

