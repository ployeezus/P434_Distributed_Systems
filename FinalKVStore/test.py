import socket
from threading import Thread

from eventual import getSet

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True: 
        connectionSocket, addr = s.accept()
        new_thread = Thread(getSet, connectionSocket)
        new_thread.start()
        new_thread.join()
        