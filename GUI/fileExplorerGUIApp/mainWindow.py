# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QObject, pyqtSlot


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setWordWrap(True)
        self.Title.setObjectName("Title")
        self.horizontalLayout_2.addWidget(self.Title)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fileName.setFont(font)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.filePath = QtWidgets.QLineEdit(self.frame)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout.addWidget(self.filePath)
        self.browseButton = QtWidgets.QPushButton(self.frame)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.FileContent = QtWidgets.QTextEdit(self.frame)
        self.FileContent.setObjectName("FileContent")
        self.gridLayout.addWidget(self.FileContent, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.writeButton = QtWidgets.QPushButton(self.frame)
        self.writeButton.setObjectName("writeButton")
        self.gridLayout.addWidget(self.writeButton, 2, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.browseButton.clicked.connect(self.browseSlot)
        self.writeButton.clicked.connect(self.writeDocSlot)
        self.filePath.returnPressed.connect(self.returnPressedSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "File Explorer"))
        self.fileName.setText(_translate("MainWindow", "File Name"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.writeButton.setText(_translate("MainWindow", "Write To  Document"))

    #This is a decorator applied to 
    # Python methods of a QObject that marks them as Qt slots.
    @pyqtSlot()
    def returnPressedSlot(self):
        pass
        
    @pyqtSlot()
    def writeDocSlot(self):
        pass

    @pyqtSlot()
    def browseSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
