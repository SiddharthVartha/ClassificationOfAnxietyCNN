from multiprocessing import Event
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
#from playsound import playsound 
import pyautogui
import sys
width, height= pyautogui.size()
print(width,height)

class Ui_MainWindow1(QWidget,object):   
    def __init__(self):
        super().__init__()    
        
    
    def openAnother(self):
        from SecondPage import Ui_MainWindow2
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.close()
        MainWindow1.close()   
    
    def setupUi(self, MainWindow1):    
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(width,height)
        MainWindow1.setStyleSheet("QMainWindow{\n"
"margin:0px;\n"
"padding:0px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #03c8a8, stop:1 #89d8d3);\n"
"}\n"
"")
        MainWindow1.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("margin:0px;\n"
"padding:0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"Stress_Free.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.anim = QPropertyAnimation(self.label, b"geometry")
        self.anim.setDuration(2500)
        #self.anim.setStartValue(QRect(-width,0,0,0))
        #self.anim.setEndValue(QRect(0,0, width, int(height*2/5)))
        self.anim.setStartValue(QRect(0,0,width,-int(height*2/5)))
        self.anim.setEndValue(QRect(0,0, width, int(height*2/5)))
        self.anim.start() 
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.anim2 = QPropertyAnimation(self.frame_2, b"geometry")
        self.anim2.setDuration(2500)
        #self.anim2.setStartValue(QRect(-1,1,0,0))
        #self.anim2.setStartValue(QRect(width*2,0,0,0))
        #self.anim2.setEndValue(QRect(1,int(height*2/5), width, int(height*2/5)))
        self.anim2.setStartValue(QRect(int(width/2),height,0,height*2))
        self.anim2.setEndValue(QRect(1,int(height*2/5), width, int(height*2/5)))
        self.anim2.start() 
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.StartTest = QtWidgets.QPushButton(self.frame_4)
        self.StartTest.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartTest.sizePolicy().hasHeightForWidth())
        self.StartTest.setSizePolicy(sizePolicy)
        self.StartTest.setMaximumSize(QtCore.QSize(146, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.StartTest.setFont(font)
        self.StartTest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartTest.setTabletTracking(False)
        self.StartTest.setAcceptDrops(False)
        self.StartTest.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StartTest.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"border:2px dashed black;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"color:red;\n"
"border:2px dashed white;\n"
"}")
        self.StartTest.setIconSize(QtCore.QSize(30, 30))
        self.StartTest.setShortcut("")
        self.StartTest.setAutoDefault(False)
        self.StartTest.setObjectName("StartTest")
        self.gridLayout_5.addWidget(self.StartTest, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 7, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 2, 3, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 6, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1207, 26))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)
        self.StartTest.clicked.connect(self.openAnother)
        if(True):
                print(pyautogui.position())
        app1.aboutToQuit.connect(self.closeEvent)
    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Welcome"))
        self.StartTest.setText(_translate("MainWindow1", "Start Test"))
        self.label_2.setText(_translate("MainWindow1", "Stress is a feeling of emotional or physical tension. It can come from any event or thought that makes you feel frustrated, angry, or nervous.Stress is your body's reaction to a challenge or demand.\n"
"Stress happens when we lose control of given situation. Stress is no fun in any way it makes us feel a bit frayed around the edges.As it's conventional side it makes us motivated to work and gain more fight back to gain control."))
        self.label_3.setText(_translate("MainWindow1", "STOP TRYING TO CALM THE STORM. CALM YOURSELF THE STORM WILL PASS. - TIMBER HAWKEYE"))
        self.label_4.setText(_translate("MainWindow1", "Click Here To Test"))
    def closeEvent(self):
        #Your code here
        print('Window closed')
        sys.exit(0)

        

app1 = QtWidgets.QApplication(sys.argv)
MainWindow1 = QtWidgets.QMainWindow()
ui = Ui_MainWindow1()
ui.setupUi(MainWindow1)
#MainWindow1.showMaximized()
MainWindow1.showMaximized()
sys.exit(app1.exec_())
