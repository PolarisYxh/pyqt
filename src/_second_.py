from PyQt5.QtWidgets import *
from src.second import *
class second_(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(second_,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('second')
        self.center()

    def myshow(self,widget):
      #  widget.s
        widget.close()
        self.resize(widget.geometry().width(), widget.geometry().height())
        self.move(widget.geometry().topLeft())
       # widget.close()
        self.show()

    def center(self):
        scr = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((scr.width() - size.width()) / 2, (scr.height() - size.height()) / 2)
