from socket import *
import threading
import time
import socketserver
from _thread import *
import os.path
import sys
import socket
from threading import Thread

from eventual import getSet

# Socket  connections
serverPort = int(sys.argv[1])
serverName = 'localhost'

# need diff serverPorts for each replicas for each new consistency

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("Ready to receive \n")
serverSocket.listen()
# locks = threading.Lock()

# Initialize dictionary and make new file
kvstore = {}
file = open('ploytest.txt', 'a+')

# dont need a lock for eventual consistency

def getSet():
    #Client input received here
    sentence = connectionSocket.recv(1024).decode()

    # Checks input request type if's get or set by using split sentence
    request_type = sentence.split()[0]
    print(str(request_type))
    if str(request_type) == "set":

        keyword = sentence.split()[1]
        value = sentence.split()[2]

       # print(keyword, value)
        ## set ops
        #print(str(request_type))
        kvstore[keyword] = value

        # locks.acquire()

        file.write('%s:%s\n' % (keyword, value))
        
        print(kvstore[keyword])
        connectionSocket.send('successfully saved!'.encode())

        # read server port numbers and send to key value to that port
        f = open('serverPorts.txt', "r")
        for x in f:
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName, x))
            print(x) 
        f.close

        # locks.release()

    elif str(request_type) == "get":
        key_val = sentence[1]
        if key_val in kvstore.keys():
            val = str(kvstore[key_val])
            connectionSocket.send(val.encode())

# create diff servers for each consistency

# You get connected here 
while 1:
    connectionSocket, addr = serverSocket.accept()
    new_thread = Thread(getSet, connectionSocket)
    new_thread.start()
    new_thread.join()
        

