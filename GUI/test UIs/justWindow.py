#1st gui using pyqt5 
#this just creates a window
from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    #setting the window size
    w.resize(500,500)
    #setting the window name
    w.setWindowTitle("Test1")
    w.show()
    sys.exit(app.exec_())