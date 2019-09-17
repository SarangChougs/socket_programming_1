#Server side
import socket

print("This is server")
#creating a socket object
s = socket.socket()
print("\nSocket Created successfuly")

#reserve a port on the computer
port = 1234

#bind to the port
s.bind(('',port))
print(f"Socket binded to port-{port}")

#put the socket in listening mode
s.listen(5)
print("Socket is listening")

#establish connetion with the client
c,addr = s.accept()
print(f"Got connetion from >>{addr}")

#a forever loop until we interrupt it or and error occurs
while True:
    #send a thankyou message to the client
    mssg = input("Enter the message to send to client>>")
    #get out of the loop if message is bye
    if(mssg == 'bye'):
        print("Thank you for joining the connection.\n Connection is closed.")
        break
    #sending the message
    c.sendall(bytes(mssg,'UTF-8'))
    #receving the message
    print(str(addr) + ">>" + c.recv(1024).decode())

#close the connection from the client
c.close()