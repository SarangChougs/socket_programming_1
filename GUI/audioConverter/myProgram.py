from PyQt5 import QtWidgets
from Main import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import sys

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.myButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        self.ui.label.setText("Button Clicked")
        self.filename,_ = QFileDialog.getOpenFileName()
        if self.filename:
            self.ui.lineEdit.setText("Reading " + self.filename)
            self.ui.lineEdit.repaint()


app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())