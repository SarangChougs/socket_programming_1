# Server side code to send a file to the client

import socket

s = socket.socket()             #Creating the socket

host = socket.gethostname()     #setting host automatically
port = 6666                     #and port

s.bind((host,port))             #binding server to the host and port

s.listen(5)                     #listening for the connections
print("Server is listening...")


while True:
    client,addr = s.accept()    #accepting the connectioin form the client
    print(f"Got connection from {addr}")

    data = client.recv(1024).decode()   #receiving data
    print(f"From Client>> {data}")

    filename = 'test.txt'
    f =open(filename,'rb')
    l = f.read(1024)

    while(l):
        client.send(l)
        print('sending >>',repr(l.decode()))
        l = f.read(1024)
        
    f.close()

    print("Done sending")
    break

client.send("Thank you for connecting".encode())
client.close()
