from socket import *
import time

listen = open('listen.txt','a')
recive = open('recive.txt','a')
s = socket(AF_INET,SOCK_STREAM)
l = socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',9150))
l.bind(('127.0.0.1',7777))
l.listen(5)
c,a = l.accept()

while True:
    listining = c.recv(4096)
    print listining
    listen.write(listining+str('\n'))
    listen.write(time.ctime()+str('\n'))
    s.send(listining)
    reciving = s.recv(4096)
    print reciving
    recive.write(reciving+str('\n'))
    recive.write(time.ctime()+str('\n'))
    c.send(reciving)
