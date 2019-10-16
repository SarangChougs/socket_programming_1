# Client side to download a file from the server using TCP
# code used from youtube link: https://www.youtube.com/watch?v=LJTaPaFGmM4

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    #taking filename from the user
    filename = input("Filename? ->")
    #if filename == q then quit
    if filename != 'q':
        #sending the file name to server
        s.send(bytes(filename,'UTF-8'))
        #receiving the response from the server that whether the file exists or not
        data = s.recv(1024).decode('UTF-8')
        #if file exists then display file info and ask for download
        if data[:6] == 'EXISTS':
            print("data ->", data)
            filesize = int(data[9:])
            message = input("File Exists. "+str(filesize)+' bytes, download? (Y/N)? ->')
            #if Y then begin download
            if message == 'Y'or'y':
                print("Downloading started...")
                s.send(bytes('OK','UTF-8'))
                #create a file  with prefix 'new_ ' to save the incoming data
                f = open('new_'+filename, 'wb')
                #receiving 4096 chunks of data at a time
                data = s.recv(4096)
                totalRecv = len(data)
                f.write(data)
                #if data more than 1 chunk then receiving more data
                while totalRecv < filesize:
                    data = s.recv(4096)
                    totalRecv += len(data)
                    f.write(data)
                    received = (totalRecv/filesize)*100
                print("Download Complete!")
        else:
             print("File does not Exist!")
    s.close()

if __name__ == "__main__":
    Main()

        