from socket import *

HOST = 'rocky.olin.edu'           # the remote host
PORT = 50007                      # the same port used by the server

csock = socket(AF_INET, SOCK_STREAM)
csock.connect((HOST, PORT))
print 'Client connected to: ', csock.getpeername()

csock.send('Hello, world')
data = csock.recv(1024)

csock.close()
print 'Client received', `data`
