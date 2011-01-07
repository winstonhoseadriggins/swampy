from socket import *

HOST = ''                         # empty string means the local host
PORT = 50007                      # arbitrary non-privileged port

lsock = socket(AF_INET, SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen(1)
csock, addr = lsock.accept()
print 'Server connected to:', csock.getpeername()

while 1:
    data = csock.recv(1024)
    if not data: break
    print 'Server received', `data`
    csock.send(data)
csock.close()
lsock.close()
