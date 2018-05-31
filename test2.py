from socket import *
from urllib import *
import time
s = socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',9050))
t = open('f.txt','r')
reads = t.read()
s.send(reads)
print reads
re = s.recv(4096)
request = '''GET index.html HTTP/1.1
Host: "www.duckduckgo.com"
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache'''
print re
host_name = 'www.duckduckgo.com'
ip = gethostbyname(host_name)
ip_array = ip.split('.')
ip_in_hex = []
for i in range(len(ip_array)):
    ip_in_hex.append(hex(int(ip_array[i])))
socks_request1 = '0x040x010x000x50'
socks_request3 = '0x670x00'
socks_request2 = ''
for i in range(len(ip_in_hex)):
    socks_request2=socks_request2+str(ip_in_hex[i])
socks_request = socks_request1+socks_request2+socks_request3
print socks_request
#if '0x00' in re:
s.send(socks_request)
#s.send(reads)
print '[+] sent the socks request'
re = s.recv(4096)
print re
#print '[+] sent the socks request'
#if '0x00' in re:
time.sleep(1)
s.send(request)
print '[+] sent the request'
response = s.recv(4096)
print response
