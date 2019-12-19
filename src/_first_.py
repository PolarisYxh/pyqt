import os
import cv2
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from src.first import *
class first_(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(first_,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('first')
        self.label_2.setScaledContents(True)
        scr = QDesktopWidget().screenGeometry()
        self.resize(scr.width(),scr.height())
        self.center()
        self.pushButton_5.clicked.connect(self.openfile)
        self.pushButton_6.clicked.connect(self.myclose)
        self.stopEvent = threading.Event()
        self.stopEvent.clear()


    def center(self):
        scr = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #Qsize.
        self.move((scr.width()-size.width())/2,(scr.height()-size.height())/2)
        #self.move()

    def myshow(self, widget):
        widget.close()
       # self.move(widget.geometry().topLeft())
       # self.resize(widget.geometry().width(),widget.geometry().height())
        self.show()

    def openfile(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        if fileName == "" :
            print('hhhh')
        else:
            self.stopEvent = threading.Event()
            self.stopEvent.clear()
            self.toDisplay(fileName)

    def toDisplay(self,fileName):
        print('here')
        self.cap = cv2.VideoCapture(fileName)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        th = threading.Thread(target=self.Display)
        th.start()

    def Display(self):
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(True)
        self.label.setText('zhengzaijisuanzhong......')


        while self.cap.isOpened():
            success, frame = self.cap.read()
            # RGB转BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.label_2.setPixmap(QPixmap.fromImage(img))
            cv2.waitKey(int(1000 / self.frameRate))
            # 判断关闭事件是否已触发
            if True == self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.label_2.clear()
                self.pushButton_6.setEnabled(False)
                self.pushButton_5.setEnabled(True)
                break


    def myclose(self):
        self.stopEvent.set()
        self.label.setText('jisuanwancheng!!!')
