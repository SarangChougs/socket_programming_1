# model.py
# This is the model part of the Model-View-Controller
# The class holds the name of a text file and its contents.
# Both the name and the contents can be modified in the GUI
# and updated through methods of this model.# model.py
# This is the model part of the Model-View-Controller
# The class holds the name of a text file and its contents.
# Both the name and the contents can be modified in the GUI
# and updated through methods of this model.


import socket

class Model:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None
        self.fileContent = ""
        self.host = ""
        self.port = ""

    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid( fileName ):
            self.fileName = fileName
            self.fileContents = open( fileName, 'r' ).read()
        else:
            self.fileContents = ""
            self.fileName = ""
            
    def getFileName( self ):
        '''
        Returns the file name.
        '''
        return self.fileName

    def getFileContents( self ):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents
    
    def sendFile( self, filename, filecontent ):
        '''
        Sends the selected file to the server
        '''
        pass

    def connectToServer( self,serverIp,serverPort ):
        ''' 
        Connects the client to the requested Server...
        '''
        self.ip = serverIp
        self.port = serverPort
        try :
            s = socket.socket()
            s.connect((self.ip,self.port))
        except Exception as e:
            return e

    def disconnetFromServer( self,server ):
        try:
            server.close()
        except Exception as e:
            return e

