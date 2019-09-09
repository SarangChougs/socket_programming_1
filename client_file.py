# Client program to receive file using ftp server

import socket

s =socket.socket()

host = socket.gethostname()
port = 6666

s.connect((host,port)) 

s.send("Hello server!".encode())

with open('received file', 'wb') as f:
    print("File Opened.")
    print("Receiving data...")
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

print("successfully received the file")
s.close()
print("Connection closed")

