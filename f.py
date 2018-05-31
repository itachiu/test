from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(('127.0.0.1',7777))
f = open('f.txt','a')
g = open('g.txt','a')
s.listen(5)
se = socket(AF_INET,SOCK_STREAM)
se.connect(('127.0.0.1',9050))

c,a = s.accept()

while True:
    l = c.recv(4096)
    #f.write(str(l))
    print str(l)
    se.send(l)
    li = se.recv(4096)
    print str(li)
    #g.write(str(li))
    


