# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Empty\Desktop\Launcher SCFA\Version v3\play_1.ui'
#
# Created: Wed Mar 25 03:27:13 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(327, 195)
        Form.setStyleSheet("QWidget{\n"
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
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, 50, 361, 39))
        self.label.setStyleSheet("color white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 110, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "SCFA not determined!\n"
" Find SCFA on main window", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Ok", None, QtGui.QApplication.UnicodeUTF8))


    def __init__(self):
        import sys
        #app = QtGui.QApplication(sys.argv)
        super(Ui_Form, self).__init__()
        #Form = QtGui.QWidget()
        #ui = Ui_Form()
        #ui.setupUi(Form)
        #Form.show()
        #sys.exit(app.exec_())

