from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import os, sys, threading
import urllib.request
from launcher_2 import Ui_Dialog
from play_1 import Ui_Form
from check import Ui_Form_2
from MainThread import MainThread


'''
if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

'''

    
#Create application
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ[" QT_SCREEN_SCALE_FACTORS"] = "1"
os.environ[" QT_ENABLE_HIGHDPI_SCALING"] = "1"
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
app = QApplication(sys.argv)



#Create Dialog and init UI
Dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#Hook logic
filePath = '0'

def bp_1_play():

    if filePath != '0' and filePath != '':
        print(filePath)
        directory_exe = filePath + '\\bin\\SupremeCommander.exe'
        print(directory_exe)
        os.startfile(r'%s' % directory_exe)
    else:
        Dialog.Form = QWidget()
        Dialog.w1 = Ui_Form()
        Dialog.w1.setupUi(Dialog.Form)
        Dialog.Form.show()
        Dialog.w1.pushButton.clicked.connect(bp_cancel_play)
    
def bp_cancel_play():
    Dialog.Form.close()
def bp_cancel_check():
    Dialog.Form_2.close()

def bp_update_check():
    
    
    if filePath != '0' and filePath != '':
        Dialog.w2.pushButton.setEnabled(False)
        list_lock = threading.Lock()
        thread = MainThread(filePath, Dialog.w2.label, version_base, version_new, ui.label_2, 1, file_id)
        thread.start()
    else:
        Dialog.Form = QWidget()
        Dialog.w1 = Ui_Form()
        Dialog.w1.setupUi(Dialog.Form)
        Dialog.Form.show()
        Dialog.w1.pushButton.clicked.connect(bp_cancel_play)

def bp_update_264():
    if filePath != '0' and filePath != '':
        Dialog.w2.pushButton.setEnabled(False)
        list_lock = threading.Lock()
        file_id = '1hNRfIMZQGQVdOi_ahm4PNE0bvqASmSb6'
        thread = MainThread(filePath, Dialog.w2.label, '0.0.0', '2.6.4', ui.label_2, 1, file_id)
        thread.start()
    else:
        Dialog.Form = QWidget()
        Dialog.w1 = Ui_Form()
        Dialog.w1.setupUi(Dialog.Form)
        Dialog.Form.show()
        Dialog.w1.pushButton.clicked.connect(bp_cancel_play)
def bp_update_67():
    if filePath != '0' and filePath != '':
        Dialog.w2.pushButton.setEnabled(False)
        list_lock = threading.Lock()
        file_id = '1uoG9XtpZeNOvsbpDhyh3swxO1xzi6p_Y'
        thread = MainThread(filePath, Dialog.w2.label, '0.0.0', '0.6.7', ui.label_2, 1, file_id)
        thread.start()
    else:
        Dialog.Form = QWidget()
        Dialog.w1 = Ui_Form()
        Dialog.w1.setupUi(Dialog.Form)
        Dialog.Form.show()
        Dialog.w1.pushButton.clicked.connect(bp_cancel_play)
def bp_delete():
    Dialog.w2.pushButton.setEnabled(False)
    list_lock = threading.Lock()
    thread = MainThread(filePath, Dialog.w2.label, version_base, '0.0.0', ui.label_2, 2)
    thread.start()
    ui.label_2.setText(version_base)

    


def bp_2_check():
    global version_base
    #https://docs.google.com/document/d/1WtkWnwzgNaNfx2vrDWfp85Gu5WvaHyci_NAU29SLpb4/edit?usp=sharing
    version = urllib.request.urlopen("https://drive.google.com/uc?export=download&id=" + ver_id).read()
    print(version)
    f = open("version.txt", "wb")
    f.write(version)
    f.close()

    handle = open("version.txt", "r")
    global version_new
    version_new = handle.read()
    handle.close() 

    if version_new != '0' and version_new != '':
        #???????? ?????????????????? ???????????? 
        #???????? ???????????? ?????????????????? ???? ?????????? ?????????????????? ?????? ???????????? ?????????????????? 
        #???????? ??????, ???? ???????????????????? ?????????????? ??????????????????
        

        a = [int(s) for s in version_base.split('.')]
        version_base_int = 0
        version_base_int += a[0]*100 + a[1]*10 + a[2]
        a = [int(s) for s in version_new.split('.')]
        version_new_int = 0
        version_new_int += a[0]*100 + a[1]*10 + a[2]
        print(version_new_int)
        print(version_base_int)

        if version_base_int < version_new_int:
            Dialog.Form_2 = QWidget()
            Dialog.w2 = Ui_Form_2()
            Dialog.w2.setupUi(Dialog.Form_2)
            Dialog.Form_2.show()
            Dialog.w2.pushButton_2.clicked.connect(bp_cancel_check)
            Dialog.w2.pushButton.clicked.connect(bp_update_check)
                 
        else:
            Dialog.Form_2 = QWidget()
            Dialog.w2 = Ui_Form_2()
            Dialog.w2.setupUi(Dialog.Form_2)
            Dialog.Form_2.show()
            Dialog.w2.pushButton.setEnabled(False)
            Dialog.w2.pushButton_2.clicked.connect(bp_cancel_check)
            Dialog.w2.label.setText('You have last version')
        


def bp_3_browse():
    global filePath
    filePath = QFileDialog.getExistingDirectory(Dialog,"Select Directory","C:\\Program Files (x86)\\Steam\\steamapps\\common\\Supreme Commander Forged Alliance")
    if filePath != '0':
        ui.lineEdit.setText(filePath)

def bp_4_browse():
    filePath = ui.lineEdit.text()
    f = open("settings.txt", "w")
    f.write(filePath)
    f.close()

def bp_5_delete():

    if filePath != '0' and filePath != '':
        Dialog.Form_2 = QWidget()
        Dialog.w2 = Ui_Form_2()
        Dialog.w2.setupUi(Dialog.Form_2)
        Dialog.Form_2.show()
        Dialog.Form_2.setWindowTitle(QCoreApplication.translate("Form_2", u"Delete SC", None))
        Dialog.w2.pushButton.setText(QCoreApplication.translate("Form_2", u"Delete", None))
        Dialog.w2.label.setText('Delete SC Legacy?')
        Dialog.w2.pushButton_2.clicked.connect(bp_cancel_check)
        Dialog.w2.pushButton.clicked.connect(bp_delete)
    else:
        Dialog.Form = QWidget()
        Dialog.w1 = Ui_Form()
        Dialog.w1.setupUi(Dialog.Form)
        Dialog.Form.show()
        Dialog.w1.pushButton.clicked.connect(bp_cancel_play)

def bp_6_confirm_id_p():
    global file_id 
    file_id = ui.lineEdit_2.text()
    f = open("patch_id.txt", "w")
    f.write(file_id)
    f.close()
def bp_7_confirm_id_v():
    global ver_id
    ver_id = ui.lineEdit_3.text()
    f = open("version_id.txt", "w")
    f.write(ver_id)
    f.close()
def bp_8_264():

            Dialog.Form_2 = QWidget()
            Dialog.w2 = Ui_Form_2()
            Dialog.w2.setupUi(Dialog.Form_2)
            Dialog.w2.label.setText('Are you sure you want \nto install that version?')
            Dialog.Form_2.show()
            Dialog.w2.pushButton_2.clicked.connect(bp_cancel_check)
            Dialog.w2.pushButton.clicked.connect(bp_update_264)
def bp_9_67():
            Dialog.Form_2 = QWidget()
            Dialog.w2 = Ui_Form_2()
            Dialog.w2.setupUi(Dialog.Form_2)
            Dialog.w2.label.setText('Are you sure you want \nto install that version?')
            Dialog.Form_2.show()
            Dialog.w2.pushButton_2.clicked.connect(bp_cancel_check)
            Dialog.w2.pushButton.clicked.connect(bp_update_67)

  
#file_id = '1J_h1W_ogDElBuU_OZKVQ6RdntchxIKN2'
#ver_id = '1Xv8dfIFf51RJ7XL0ldpxOY_W2gFhqPL3'

try:
    handle = open("version_id.txt", "r")
    ver_id = handle.read()
    handle.close()
    ui.lineEdit_3.setText(ver_id)    
except IOError:
    ver_id = '0'

try:
    handle = open("patch_id.txt", "r")
    file_id = handle.read()
    handle.close()
    ui.lineEdit_2.setText(file_id)    
except IOError:
    file_id = '0'


try:
    handle = open("settings.txt", "r")
    filePath = handle.read()
    handle.close()
    ui.lineEdit.setText(filePath)    
except IOError:
    filePath = '0'

try:
    handle = open("version.txt", "r")
    version_base = handle.read()
    handle.close()   
except IOError:
    version_base = '0.0.0'
'''
#Dialog.setPixmap(QPixmap("com_11.jpg"))
print(os.path.abspath("com_11.jpg"))
pixmap = QPixmap(os.getcwd() + "\\com_11.jpg")
ui.label_9.setPixmap(pixmap)
'''

ui.label_3.setText('<a style="color:white; "href="https://www.youtube.com/channel/UCBNDD56Y3-lKx2N5qsbOdaA"> Youtube Channel - ImperatoR Arthas_DK</a>') 
ui.label_3.setOpenExternalLinks(True)
ui.plainTextEdit.setPlainText(
"Important: this modpack plays only 2x speed\n"
"\n"
"Mods to be included\n"
"- RelNukes -\n"
"- BrewLAN - \n"
"- BrewLAN Research - \n"
"- BrewLAN Bubble - \n"
"- BrewLAN Carre - \n"
"- Total Mayhem v1.21 \n"
"- 4th Dimension 2.12- FA Version \n"
"- Wyvern Battle Pack - \n"
"- BlackOps Unleashed - \n"
"- BlackOps Unleashed Balance Changes - \n" 
"- Black Ops Adv Command Units - \n"
"- Black Ops Special Weapons - \n"
"- Black Ops Global Icon Mod - \n"
"- Shields V3.6 - \n"
"- AutoTML -\n"
"- Upgradeable HC-Plant \n"
"- Firey Exposions mod 2.6 - \n" 
"- Nuke Collide \n"
"- Antares Battle Pack \n"
"- Experimental Icons \n"
"- Mass Point RNG")

ui.label_2.setText(version_base) 
ui.pushButton.clicked.connect(bp_1_play)
ui.pushButton_2.clicked.connect(bp_2_check)
ui.pushButton_3.clicked.connect(bp_3_browse)
ui.pushButton_4.clicked.connect(bp_4_browse)
ui.pushButton_5.clicked.connect(bp_5_delete)
ui.pushButton_6.clicked.connect(bp_6_confirm_id_p)
ui.pushButton_7.clicked.connect(bp_7_confirm_id_v)
ui.pushButton_8.clicked.connect(bp_8_264)
ui.pushButton_9.clicked.connect(bp_9_67)
#Run main loop
sys.exit(app.exec_())
