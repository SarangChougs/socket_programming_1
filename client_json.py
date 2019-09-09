# Client program to send file using ftp server and json

import socket
import json

s =socket.socket()

host = socket.gethostname()
port = 6666

data = "this is test data"
s.connect((host,port)) 

s.send(bytes(json.dumps(data),'UTF-8'))

filename = 'test_json.txt'
f =open(filename,'r')
l = f.read(1024)
while(l):
    s.send(bytes(json.dumps(l),'UTF-8'))
    #print('sending >>',repr(l.decode()))
    l = f.read(1024)
f.close()

print("successfully sent the file")
s.close()
print("Connection closed")

