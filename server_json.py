# a server side program to send data using json 

import socket
import json

s = socket.socket()

host = socket.gethostname()     #setting host automatically = 6666                     
port = 6666                     #and port address

s.bind((host,port))             #binding server to the host and port

s.listen(5)                     #listening for the connections
print("Server is listening...")

while True:
    client,addr = s.accept()    #accepting the connectioin form the client
    print(f"Got connection from {addr}")

    try:
        with open('received_json file', 'w') as f:
            print("File Opened.")
            print("Receiving data...")
            while True:
                data = json.loads(client.recv(1024).decode('UTF-8'))
                if not data:
                    break
                f.write(data)
        #sending some ok message back
        client.sendall(bytes(json.dumps({'return':'ok'}), 'UTF-8'))

    except Exception as e:
        print("Error in receiving file: ",e)

    print("Done receiving")
    break

client.close()