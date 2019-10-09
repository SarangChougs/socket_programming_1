# MyApp.py
#the Controller class , the starting point of the program
# Editable UI version of the MVC application.
# Inherits from the Ui_MainWindow class defined in mainwindow.py.
# Provides functionality to the 3 interactive widgets (2 push-buttons,
# and 1 line-edit).
# The class maintains a reference to the model that implements the logic
# of the app.  The model is defined in class Model, in model.py.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from mainWindow import Ui_MainWindow #importing the ui class
import sys
from model import Model  #importing the model class

class MainWindowUIClass( Ui_MainWindow ):
    def __init__( self ):
        '''Initialize the super class'''
        super().__init__()
        self.model = Model() #creating the reference of the model class
        
    def setupUi( self, MW ):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi( MW )

        # close the lower part of the splitter to hide the 
        # debug window under normal operations
        self.splitter.setSizes([300, 0])

    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.debugTextBrowser.append( msg )

    def refreshAll( self ):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change.  Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''

        #set the filepath text box to the path of the file choosen 
        self.filePath.setText( self.model.getFileName() )
        #set the file content text box to the contents of the file opened
        self.FileContent.setText( self.model.getFileContents() )

    # slot
    def returnPressedSlot( self ):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''

        #getting the file name from the file path text box
        fileName =  self.lineEdit.text()
        #checking if the file name is valid if entered by the user
        if self.model.isValid( fileName ):
            self.model.setFileName( self.lineEdit.text() )
            self.refreshAll()
        #if the file name is not valid then showing the warning box
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.filePath.setText( "" )
            self.refreshAll()
            self.debugPrint( "Invalid file specified: " + fileName  )

        self.debugPrint( "RETURN key pressed in LineEdit widget" )

    # slot
    def writeDocSlot( self ):
        ''' Called when the user presses the Write-Doc button.
        '''

        #write the content of the file content text box in the file
        self.model.writeDoc( self.FileContent.toPlainText() )
        self.debugPrint( "WriteDoc button pressed!" )

    # slot
    def browseSlot( self ):
        ''' Called when the user presses the Browse button
        '''

        #getting the file from the browse button using file explorer
        self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","All Files (*);;Python Files (*.py)",options=options)
        if fileName:
            self.debugPrint( "setting file name: " + fileName )
            self.model.setFileName( fileName )
            self.refreshAll()



def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()