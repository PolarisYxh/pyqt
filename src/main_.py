from src.main import Ui_MainWindow
from src._first_ import *
from src._second_ import *
from src._third_ import *


class main_(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(main_, self).__init__(parent)
        self.setupUi(self)
       # self.menubar.addMenu('>????')
       # menu = self.menubar.addMenu('menu')
        #first = menu.
        self.menubar.triggered[QAction].connect(self.change)



        self.setWindowTitle('haah')

    def on_pushButton_enter_clicked(self):
        self.frame1.setVisible(True)
        self.frame.setVisible(False)

    def on_pushButton_enter_clicked_1(self):
        self.frame1.setVisible(False)
        self.frame.setVisible(True)

    def change(self,q):
        print(q.text())
        if q.text() == 'first':
            first = first_()
            first.show()
            sys.exit(app.exec_())




if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
  #  ui1 = first_()
  #  ui2 = second_()
  #  ui1.pushButton_2.clicked.connect(lambda:ui2.myshow(ui1))
  #  ui2.pushButton.clicked.connect(lambda:ui1.myshow(ui2))
   # ui1.show()
    ui3 = third_()
    ui3.show()
    ui3.openGLWidget.show()
    sys.exit(app.exec_())