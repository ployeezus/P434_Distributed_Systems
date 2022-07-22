from socket import *
from xxlimited import new

# Socket  connections
serverPort = 1206
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("127.0.0.1",serverPort))
print("Ready to receive \n")
serverSocket.listen()

#You get connected 
while 1:
    connectionSocket, addr = serverSocket.accept()
    # Client input received here
    sentence = connectionSocket.recv(1024)
    ''''
        Code for get and set would go here
    '''
    #modified the input
    capitalizedSentence = sentence.lower()
    sent_text = "MapReuce is ready and ran!".encode('utf-8')
    newModified = str(capitalizedSentence, 'utf-8')
    print(sent_text) # What it sends to the client
    print()
    print()
    print('New:', newModified) # What it runs
    #sending it back to client 

    ''' This is where mapper is going to run'''

    try:
        from totalmap import *
        readingFile(newModified)
        
    except:
        print("Something is totally wrong. Retry!")



    connectionSocket.send(sent_text)
    #closing connection of the client, server will still run. Another client can join and connect
    connectionSocket.close()