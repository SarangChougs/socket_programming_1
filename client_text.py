#Client side

#Importing the required library
import socket

print("This is Client")
#Create the socket
s = socket.socket()

#the port to which we want to connect
port = 1234
ip = socket.gethostname()

#connect to the server
s.connect((ip,port))

try:
    while True:
        #receiving the data from server
        print( "(server)>>" + s.recv(1024).decode())
        #sending the data to the server
        mssg = input("Enter a message to send to server>>")
        s.sendall(bytes(mssg,'UTF-8'))
except Exception as e:
    print("Connection terminated by server.")
    s.close()
#close the connection
s.close()