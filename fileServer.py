# a program to implement TCP file server
# used code from youtube link: https://www.youtube.com/watch?v=LJTaPaFGmM4

import socket
import threading
import os

#the function to return a requested file
def RetrFile(sock):
    #receiving the filename from the client
    filename = sock.recv(1024).decode('UTF-8')
    try:
        #if file exists then sending file name
        if os.path.isfile(filename):
            sock.send(bytes("EXISTS : " + str(os.path.getsize(filename)),'UTF-8'))
            #receiving responce from the client
            userResponse = sock.recv(1024).decode('UTF-8')
            #if user says 'OK' then sending the file in chuncks of 4096 bytes
            if userResponse[:2] == 'OK':
                with open(filename,'rb') as f:
                    bytesToSend = f.read(4096)
                    sock.send(bytesToSend)
                    while bytesToSend != "":
                        bytesToSend = f.read(4096)
                        sock.send(bytesToSend)
        else:
            sock.send(bytes("ERROR",'UTF-8'))
    except Exception as e:
        print("ERROR in sending file: ",e)
    sock.close()

def Main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    print("Server started...")
    while True:
        c,addr = s.accept()
        print("Client connected <" + str(addr) + ">")
        RetrFile(c)
        # t = threading.Thread(target = RetrFile,args = ('retrThread',c))
        # t.start()
    s.close()

if __name__ == "__main__":
        Main()
