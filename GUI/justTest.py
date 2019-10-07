#Adding textbox in the pyqt window
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    #setting the window size
    w.resize(300,300)
    #setting window title
    w.setWindowTitle("Chatbox")
    w.show()
    sys.exit(app.exec_())
    #creating a mssg box
    mssgBox = QMessageBox()
    mssgBox.setText("This is a message box.")
    mssgBox.setDetailedText("This window displays a message box.")
    mssgBox.exec_()