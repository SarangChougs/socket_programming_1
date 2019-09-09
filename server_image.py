# A server side program to send a image to the client using tcp socket

#importing the libraries
import socket

#creating the socket
server_socket = socket.socket()

#initializing the host and port address
host = socket.gethostname()
port = 6666

#including the image
image = 'imageTest.png'

#starting the server to the port
server_socket.bind((host,port))
server_socket.listen(10)
print(">> Server is listening")

#making the image ready for transfer
while (True):
    
    #accepting the connection
    client,addr = server_socket.accept() 
    print(f">> Got connection from > {addr}")

    #open the image
    try:
        myfile = open(image,'rb')
        byte = myfile.read()
        size = len(byte)
        send = 'SIZE '+ str(size)
        print(">>Image opened succesfully.")
    except Exception as e:
        print(">>Error in opening image file.")

    try:
        #send the image size to client
        print(">>sending the file")
        client.sendall(bytes(send,'UTF-8'))
        answer = client.recv(4096).decode()
        print(f">> Answer = {answer}")

        #sending image to client
        if answer == 'GOT SIZE':
            client.sendall(byte)

            #checking what client send
            answer = client.recv(4096).decode()
            print(f">> Answer = {answer}")
            if answer == 'GOT IMAGE':
                client.sendall(bytes('Bye Bye','UTF-8'))
                print(">> Image successfully sent to client")
            
            myfile.close()
    except Exception as e:
        print("Error in sending image: ",e)
    client.close()  #closing the connection