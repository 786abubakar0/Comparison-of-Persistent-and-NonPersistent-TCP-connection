from socket import *
import time


        ###***function: receivefile***
        ### which takes ip,port and files array to receive, and makes socket to get data from server

def receivefile(serverIP,serverPort,filestoreceive):
    print("********************Non-persistent Connection creation********************")

    clientSocket = socket(AF_INET, SOCK_STREAM)         #creation of socket: AF_INET tells about ipv4 addressing and SOCK_STREAM tells about TCP socket
    serverPort = int(serverPort)
    clientSocket.connect((serverIP, serverPort))        #making connection with server
    clientSocket.send(str(len(filestoreceive)).encode())#sending list of files to receive
    clientSocket.recv(1024)                             #receving ack

    ###loops that runs times equal to number of files that client requests from server
    for filename in filestoreceive:
        print("Requesting file "+filename+" from server")
        clientSocket.send(str(filename).encode())       #sending file name that client wants to receive
        size=clientSocket.recv(1024).decode()           #receiving file size
        clientSocket.send(size.encode())                #sending ack

        rec_bytes=0                                     #variable that stores number of bytes that client has received from server
        file = open("non-persistent/"+filename, "wb")   #creating file

        ###loop that receives file data
        while rec_bytes<int(size):
            data = clientSocket.recv(1024)              #receiving data from server
            clientSocket.send(str("done").encode())     #sending ack
            file.write(data)                            #writing data to file
            rec_bytes+=1024

        clientSocket.recv(1024)                         #sending ack
        print("File "+filename+" received!")
        file.close()                                    #closing file


    clientSocket.close()                                #closing socket
    print("********************Non-persistent Connection closing********************")

                        # ************************end of function**************************#


 ###************************************main********************************************************
serverPort=input("Enter server Port:")                  #port of server at which server is ready
serverIP=input("Enter server IP:")                      #ip of server
filestoreceive=["a.jpg","b.mp3","c.txt"]                #files that client wants to receive


t1=time.time()

###loop that runs for number of files that client wants to get from server: For each file client makes new connection
for file in filestoreceive:
    t3=time.time()
    receivefile(serverIP,serverPort,[file])
    t4=time.time()
    print("Time taken for file "+file+":"+str(t4-t3))

t2=time.time()
print()
print("Total time for all files:" + str(t2-t1))