from fileinput import filename
from socket import *
from curses import raw
import sys

# Port and server info
serverName = 'localhost'
serverPort = int(sys.argv[1])

#Connecting
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# User input
sentence = input(str(r'Input set/get space key space value:')).encode("utf-8")
# set 8 ploy

#sending it to sever
clientSocket.send(sentence)

#This is where you receive info from server after connecting and sending to server
modifiedSentence = clientSocket.recv(1024)
removeString = str(modifiedSentence, 'utf-8')
print('From Server: ', removeString)
clientSocket.close()

'''
How to test it(for eventual consistency):
   1. Use the set command to set a key-value in of those port
   2. Use the get command to get a key-value from other ports of this key
   3. Check if the file has stored those key-value 
'''

'''
What you need to learn:
    1. How to start up a new thread, what is the thread
    2. What is socket programming and how does the message transmits from client to server
    3. How does client connect to the server.
    4. How can a multithread be applied in socket programming.
'''