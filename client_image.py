# Client side program to receive a image from the server.

import socket

imgcounter = 1
basename = 'imageReceived%s.png'

#creating the socket
client_socket = socket.socket()

#the host and the port
host = socket.gethostname()
port = 6666

#image name
imgcounter = 1
basename ="image%s.png"

# connecting to the server
client_socket.connect((host,port))
print(">> Connection Established.")

#starting the connection
while (True):

    try:
        #receiveing the data
        print(">>Receiving data...")
        data = client_socket.recv(4096)
        print(f"data is > {data}")
        txt = str(data)
        print("",data)

        if txt.startswith('SIZE'):
            tmp = txt.split()
            size = int(tmp[1])
            print(">> Got size.")
            client_socket.sendall(bytes('GOT SIZE', 'UTF-8'))

        elif txt.startswith('BYE'):
            client_socket.close()
            print(">>Closed the file.")

        else:
            print("Receiving image file...")
            myfile = open(basename % imgcounter, 'wb')
            data = client_socket.recv(4096000)
            if not data:
                myfile.close()
                print("file closed")
                break
            myfile.write(data)
            myfile.close()

            client_socket.sendall(bytes("GOT IMAGE",'UTF-8'))
            client_socket.close()
            print(">> Client side closed.")
            imgcounter += 1

    except Exception as e:
        print("Error in receiving file: ",e)



