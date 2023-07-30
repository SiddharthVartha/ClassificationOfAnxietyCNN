from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import *
import time
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QPixmap, QImage
import os
import time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import warnings
warnings.filterwarnings('ignore')
import pyautogui
width, height= pyautogui.size()
f=open(r"Prediction.txt", "r+")
l=f.read().split(",")
print(l)
f.seek(0)
f.truncate()  
f.write("0,0,0,0,0")
f.close()                          
class Worker2(QThread):
    ImageUpdate1= pyqtSignal(QImage)
    
    def run(self):
        self.ThreadActive=True
        self.i=1
        try:
                while(self.i):    
                    if(self.i<10):
                        frame=cv2.imread("video/ezgif-frame-00"+str(self.i)+".jpg")
                        Image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                        FlippedImage=Image  
                        ConvertToQtFormat=QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                        Pic=ConvertToQtFormat.scaled (1280, 906, Qt.KeepAspectRatio)
                        self.i+=1
                        time.sleep(0.09)
                        self.ImageUpdate1.emit(Pic)
                    if(self.i>=10 and self.i<=99):
                        frame=cv2.imread("video/ezgif-frame-0"+str(self.i)+".jpg")
                        Image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                        FlippedImage=Image  
                        ConvertToQtFormat=QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                        Pic=ConvertToQtFormat.scaled (1280, 906, Qt.KeepAspectRatio)
                        self.i+=1
                        time.sleep(0.09)
                        self.ImageUpdate1.emit(Pic)
                    if(self.i>=100):
                        frame=cv2.imread("video/ezgif-frame-"+str(self.i)+".jpg")
                        Image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                        FlippedImage=Image  
                        ConvertToQtFormat=QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                        Pic=ConvertToQtFormat.scaled (1280, 906, Qt.KeepAspectRatio)
                        self.i+=1
                        if(self.i==146):
                            self.i=1
                        time.sleep(0.09)
                        self.ImageUpdate1.emit(Pic)
                    
        except Exception as e:
            print("Except")
            print(e)
            sys.exit()
            pass

        
class Ui_MainWindow4(QtWidgets.QMainWindow,object):
    def __init__(self):
        super(Ui_MainWindow4,self).__init__()
        self.Worker2=Worker2()
        self.Worker2.start()
        self.Worker2.ImageUpdate1.connect(self.ImageUpdateSlot1)
    def ImageUpdateSlot1(self,Image):
        self.video.setPixmap(QPixmap.fromImage(Image))      
        self.video.resize(Image.width(), Image.height())           

    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.setEnabled(True)
        MainWindow4.resize(width, height)
        MainWindow4.setStyleSheet("QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #03c8a8, stop:1 #89d8d3);\n"
"margin:0px;\n"
"padding:0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMaximumSize(QtCore.QSize(width,int(height*(2/5))))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.result = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.verticalLayout_5.addWidget(self.result)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.result_value = QtWidgets.QLabel(self.frame_2)
        self.result_value.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.result_value.setFont(font)
        self.result_value.setScaledContents(True)
        self.result_value.setWordWrap(True)
        self.result_value.setObjectName("result_value")
        self.verticalLayout_6.addWidget(self.result_value)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.video = QtWidgets.QLabel(self.frame)
        self.video.setText("")
        self.video.setMaximumSize(QtCore.QSize(width,int(height*(1/2))))
        #self.video.setPixmap(QtGui.QPixmap("C:\\Users\\SIDDHARTHA\\Desktop\\sidd\\project\\GUI\\Stress_Free.jpg"))
        self.video.setScaledContents(True)
        self.video.setWordWrap(False)
        self.video.setObjectName("video")
        self.verticalLayout_2.addWidget(self.video)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMaximumSize(QtCore.QSize(width,int(height*(2/5))))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.suggestion = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.suggestion.setFont(font)
        self.suggestion.setAlignment(QtCore.Qt.AlignCenter)
        self.suggestion.setObjectName("suggestion")
        self.verticalLayout_11.addWidget(self.suggestion)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.suggestion_value = QtWidgets.QLabel(self.frame_3)
        self.suggestion_value.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.suggestion_value.setFont(font)
        self.suggestion_value.setScaledContents(True)
        self.suggestion_value.setWordWrap(True)
        self.suggestion_value.setObjectName("suggestion_value")
        self.verticalLayout_12.addWidget(self.suggestion_value)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_6.addItem(spacerItem2)
        MainWindow4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1324, 26))
        self.menubar.setObjectName("menubar")
        MainWindow4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "Result"))
        self.result.setText(_translate("MainWindow4", "Result"))
        self.result.setStyleSheet("font: 87 16pt 'Segoe UI Black';")
        self.res=""
        if((l[0]==l[1] or l[0]==l[2])):
            self.res=l[0]
        elif((l[1]==l[0] or l[1]==l[2])):
            self.res=l[1]
        elif((l[2]==l[0] or l[2]==l[1])):
            self.res=l[2]
        else:
            self.res=l[2]
        self.result_value.setText(_translate("MainWindow4", "Speech Prediction :-"+""+str(l[0])+""+" \n\n"
"Face Prediction :-"+""+str(l[2])+""+"\n\t\t     Depression:-"+""+str(l[3])+"\n"
"QnA Prediction :-"+""+str(l[1])+""+"\n\t\t     Stress:-"+""+str(l[4])+"\n"
"ANXIETY RESULT :-"+self.res+""))
        self.result_value.setStyleSheet("font: 87 14pt 'Segoe UI Black';")
        self.suggestion.setText(_translate("MainWindow4", "Suggestion"))
        self.suggestion.setStyleSheet("font: 87 14pt 'Segoe UI Black';")
        self.suggestion_value.setText(_translate("MainWindow4", "1] Take a time-out :- Practice yoga, listen to music, meditate, get a massage, or learn relaxation techniques. Stepping back from the problem helps clear your head.\n"
        "2] Talk to someone :- Tell friends and family you’re feeling overwhelmed, and let them know how they can help you. Talk to a physician or therapist for professional help. \n"
        "3] Exercise daily :- To help you feel good and maintain your health.\n"
        "4] Get enough sleep :- When stressed, your body needs additional sleep and rest.\n"
        "5] Welcome humor :- A good laugh goes a long life way."))
        self.suggestion_value.setStyleSheet("font: 63 14pt 'Segoe UI Semibold';")
        



import sys
app4 = QtWidgets.QApplication(sys.argv)
MainWindow4 = QtWidgets.QMainWindow()
ui = Ui_MainWindow4()
ui.setupUi(MainWindow4)
MainWindow4.showMaximized()
#MainWindow4.show()
#sys.exit(app4.exec_())