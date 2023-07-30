from PyQt5 import QtCore, QtGui, QtWidgets
import sounddevice as sd
from scipy.io.wavfile import write
from PyQt5.QtWidgets import *
import emotion as em
import librosa           
import numpy as np
from keras.models import model_from_json
import librosa
import cv2
import pylab
import librosa.display
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
import pyautogui
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
import os
import matplotlib.pyplot as plt
import librosa.display
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
width, height= pyautogui.size()
class Ui_MainWindow2(QWidget,object):
    
    def __init__(self):
        super().__init__()
 
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(width, height)
        MainWindow2.setStyleSheet("QMainWindow{\n"
"margin:0px;\n"
"padding:0px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #03c8a8, stop:1 #89d8d3);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"mic.jpg"))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Timer = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(9)
        self.Timer.setFont(font)
        self.Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Timer.setObjectName("Timer")
        self.verticalLayout.addWidget(self.Timer)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"margin-top:30px;\n"
"border-radius:10px;\n"
"border:2px solid;\n"
"height:100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#f5f7fa;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        self.pushButton.clicked.connect(self.rec)
    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Recording"))
        self.label.setText(_translate("MainWindow2", "Tell me about yourself :\n What is your name?\n Where do you stay?\n What do you do?"))
        self.Timer.setText(_translate("MainWindow2", "15 Sec"))
        self.pushButton.setText(_translate("MainWindow2", "Click to Start Recording"))
    def rec(self):
        Duration=5
        self.fs=22050
        self.a=sd.rec(int(Duration*self.fs),self.fs,2)
        sd.wait()
        write(r"recording0.wav",self.fs,self.a)
        file=r"recording0.wav"
        emotion_dict = {0: "angry", 1: "fearful",2: "happy", 3: "natural", 4: "sad"}
        res=[]
        json_file=open(r"model\speech_model_CNN_78_1.json", 'r')
        loaded_model_json=json_file.read()
        json_file.close()
        emotion_model=model_from_json(loaded_model_json)

        emotion_model.load_weights(r"model\speech_model_CNN_78_1.h5")
        print("Loaded model from disk")

        y, sr=librosa.load(r"recording0.wav")
        save_path=r'Speech.jpg'
        plt.axis('off')  # no axis
        plt.axes([0., 0., 1., 1.], frameon=False, xticks=[],
                yticks=[])  # Remove the white edge
        librosa.display.waveshow(y, sr=sr)
        plt.savefig("WavePlot.jpg", bbox_inches=None, pad_inches=0)
        self.label_3.setPixmap(QtGui.QPixmap(r"WavePlot.jpg"))
        mel_spectrogram=librosa.feature.melspectrogram(y,sr=44100, n_fft=4096, hop_length=441, win_length=1764, n_mels=224, fmax=20000)
        log_mel_spectrogram=librosa.power_to_db(mel_spectrogram)
        librosa.display.specshow(
        log_mel_spectrogram, x_axis="time", y_axis="mel", sr=44100)
        plt.savefig(save_path, bbox_inches=None, pad_inches=0)
        plt.close()
        # image extension .png,.jpg
        img=Image.open(r'Speech.jpg')
        new_width=256
        new_height=256
        img=img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img.save(r"resize.jpg")
        temp=cv2.imread(r"resize.jpg")
        temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
        temp=np.expand_dims(temp, axis=2)
        temp=temp/255
        crop_image=np.expand_dims(np.expand_dims(cv2.resize(temp, (256, 256)),0),axis=3).astype(np.float32)
        emotion_prediction=emotion_model.predict(crop_image)
        maxindex=int(np.argmax(emotion_prediction))
        res.append(np.argmax(emotion_prediction))
        print(emotion_dict[maxindex])
        prediction=emotion_dict[maxindex]
        if(prediction=="happy"):
            f=open(r"Prediction.txt", "r+")
            l=f.read().split(",")
            l[0]="No Anxiety"    
            update=",".join(l)
            f.seek(0)
            f.truncate()
            f.write(update)
            f.close()
            #em.happy(file)
            print("Speech happy")
        if(prediction=="sad"):
            f=open(r"Prediction.txt", "r+")
            l=f.read().split(",")
            l[0]="Anxiety"    
            update=",".join(l)
            f.seek(0)
            f.truncate()
            f.write(update)
            f.close()
            #em.sad(file)
            print("Speech sad")
        if(prediction=="natural"):
            f=open(r"Prediction.txt", "r+")
            l=f.read().split(",")
            l[0]="No Anxiety"    
            update=",".join(l)
            f.seek(0)
            f.truncate()
            f.write(update)
            f.close()
            #em.neutral(file)
            print("Speech neutral")
        if(prediction=="angry"):
            f=open(r"Prediction.txt", "r+")
            l=f.read().split(",")
            l[0]="Anxiety"    
            update=",".join(l)
            f.seek(0)
            f.truncate()
            f.write(update)
            f.close()
            #em.angry(file)
            print("Speech angry")
        if(prediction=="fearful"):
            f=open(r"Prediction.txt", "r+")
            l=f.read().split(",")
            l[0]="Anxiety"    
            update=",".join(l)
            f.seek(0)
            f.truncate()
            f.write(update)
            f.close()
            #em.fearful(file)
            print("Speech fearful")
        ok=QMessageBox.question(self, 'Completed', 'Now Go For Next Test :)',
                    QMessageBox.Ok)
        print(ok)
        if(ok==QMessageBox.Ok):
            from ThirdPageFinal_1 import Ui_MainWindow3
            print("hello")
            self.window2=QtWidgets.QMainWindow()
            self.ui2=Ui_MainWindow3()
            self.ui2.setupUi(self.window2)
            self.window2.show()
            self.window2.close()
            MainWindow2.close()            
    

   
import sys
app2 = QtWidgets.QApplication(sys.argv)
MainWindow2 = QtWidgets.QMainWindow()
ui = Ui_MainWindow2()
ui.setupUi(MainWindow2)
MainWindow2.showMaximized()
#MainWindow2.show()
#sys.exit(app2.exec_())
