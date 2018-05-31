from socket import *

s = socket(AF_INET,SOCK_STREAM)

l = socket(AF_INET,SOCK_STREAM)
b = open('b.txt','a')
t = open('t.txt','a')
l.bind(('127.0.0.1',7777))

s.connect(('127.0.0.1',9050))

l.listen(5)

c,a = l.accept()

while True:
    re = c.recv(4096)
    print '[+] request recived from browser'
    s.send(re)
    b.write(str(re))
    print '[+] request sent to tor'
    re2 = s.recv(4096)
    t.write(str(re2))
    print '[+] response recived from tor'
    c.send(re2)
    print '[+] response sent to browser'
