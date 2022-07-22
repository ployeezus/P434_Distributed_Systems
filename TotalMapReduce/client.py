from fileinput import filename
from socket import *
from curses import raw

# Port and server info
serverName = 'localhost'
serverPort = 1206

#Connecting
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# User input
num_mapper = input(str(r'Number fo Mapper: ')).encode("utf-8")
num_reducer = input(str(r'Number of Reducers: ')).encode("utf-8")
fileName = input(str(r'File Reading From: ')).encode("utf-8")
outputName = input(str(r'File to Output to: ')).encode("utf-8")

totalPut = [str(num_mapper, 'utf-8'), str(num_reducer, 'utf-8'), str(fileName, 'utf-8'), str(outputName, 'utf-8')]
#total = str(num_mapper) + ' ' + (num_reducer) + ' ' + (filename) + ' ' + (outputName) +
#sending it to sever
clientSocket.send(str(totalPut).encode('utf-8'))

#This is where you receive info from server after connecting and sending to server
modifiedSentence = clientSocket.recv(1024)
removeString = str(modifiedSentence, 'utf-8')
print('From Server: ', removeString)
clientSocket.close()

'''
    1. Ask user for number of mapper and reducer


'''