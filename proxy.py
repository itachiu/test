from socket import *

sending = open('send.txt','a')
reciving = open('recv.txt','a')

s = socket(AF_INET,SOCK_STREAM)
li = socket(AF_INET,SOCK_STREAM)

s.connect(("127.0.0.1",9050))

li.bind(("192.168.100.12",7777))

li.listen(5)
f = open('f.txt','r')
#buf ='\\'+'0x040x010x01\BB.\89\DAq\\'+'0x00'
buf = f.read()
print buf
s.send(buf)

l = s.recv(4096)
print l
if ('Z') in l:
    re = '''GET index.html HTTP/1.1
Host: "www.google.com"
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache'''
    c,a = li.accept()
    while True:
    	print '[+] listining to the client'
    	listen = c.recv(4096)
    	sending.write(str(listen))
    	print str(listen)
    	print '[+] recived request'
    	s.send(str(listen))
    	print '[+] sent the request to the tor service'
    	recive = s.recv(4096)
    	print str(recive)
    	reciving.write(str(recive))
    	print '[+] sending the recived back to tor'
    	c.send(str(recive))


