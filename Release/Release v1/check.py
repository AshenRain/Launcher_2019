# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Empty\Desktop\Launcher SCFA\Version v4\check.ui'
#
# Created: Wed Mar 25 17:35:18 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form_2(object):
    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(400, 255)
        Form_2.setStyleSheet("QWidget{\n"
"    background-color:rgb(106, 106, 106);\n"
"\n"
"\n"
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
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayoutWidget = QtGui.QWidget(Form_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 150, 321, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label = QtGui.QLabel(Form_2)
        self.label.setGeometry(QtCore.QRect(100, 60, 201, 61))
        self.label.setTextFormat(QtCore.Qt.LogText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)

    def retranslateUi(self, Form_2):
        Form_2.setWindowTitle(QtGui.QApplication.translate("Form_2", "Check_Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form_2", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form_2", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form_2", "New version is found !", None, QtGui.QApplication.UnicodeUTF8))

'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_2 = QtGui.QWidget()
    ui = Ui_Form_2()
    ui.setupUi(Form_2)
    Form_2.show()
    sys.exit(app.exec_())

'''