#Client side

#Importing the required library
import socket

#Create the socket
s = socket.socket()

#the port to which we want to connect
port = 1234
ip = socket.gethostname()

#connect to the server
s.connect((ip,port))

#print the data
print(s.recv(1024))

#close the connection
s.close()