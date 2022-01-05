from socket import *
import os
import threading

        ###***function: serve_the_client***
        ### which takes connectionSocket to use it for sending and receiving data to and from client

def serve_the_client(connectionSocket):
    print("********************Connection creation********************")
    num_of_files=connectionSocket.recv(1024).decode()   #number of files client wants to receive
    connectionSocket.send(str(num_of_files).encode())   #sending ack

    ###loop that runs equal to number of files that client wants to receive
    for i in range(int(num_of_files)):
        filename=connectionSocket.recv(1024).decode()   #getting filename to receive
        size = os.stat(filename).st_size                #getting size of file
        connectionSocket.send(str(size).encode())       #sending filesize that client requesting
        connectionSocket.recv(1024)                     #receving ack

        f = open(filename, "rb")                        #opening file that client requesting
        sent_bytes=0                                    #variable that stores number of bytes that has been sent to client

        ###loop that reads and sends data of file
        while sent_bytes<size:
            data=f.read(1024)                           #reading 1024 bytes of data
            connectionSocket.send(data)                 #sending data
            connectionSocket.recv(1024)                 #receving ack
            sent_bytes+=1024

        connectionSocket.send(str("file completed!").encode())  #file completion message sent to client
        print("File "+filename+" sent!")
        f.close()                                       #closing file

    connectionSocket.close()                            #closing socket of communication
    print("********************Connection closing********************")

                #************************end of function**************************#


 ###************************************main********************************************************
serverPort=input("Enter server Port:")                                          #port on which server will listen
ip=input("Enter server IP:")                                                    #ip address of server at which client will send request for data
serverSocket = socket(AF_INET, SOCK_STREAM)                                     #creation of tcp socket: AF_INET telling addressing is of ipv4, SOCK_STREAM telling about tcp protocol
serverPort = int(serverPort)
serverSocket.bind((ip, serverPort))                                             #binding socket to ip and port
serverSocket.listen(40)                                                         #socket starts listening

print("--------------------------------------------------------------------------")
print("------------------------------Server Started------------------------------")
print("--------------------------------------------------------------------------")

    ###loop that accepts the connection request from client and pass it to thread and again ready to accept the client request
while True:
    connectionSocket, clientAddress = serverSocket.accept()                     #accepting client request
    th=threading.Thread(target=serve_the_client,args=[connectionSocket])        #creating thread for client request and running server_the_client method
    th.start()                                                                  #starting the thread