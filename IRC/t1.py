from socket import *
import threading
import time

s = socket(AF_INET,SOCK_STREAM)

s.connect(('130.185.232.126',6667))

server_msg = s.recv(4096)
sends = 'PASS none\n'+'NICK test007\n'+'USER bla bla bla bla'
#s.send(sends)
#print server_msg
#s.send(raw_input('test# '))
#server_msg = s.recv(4096)
'''while True:
    if not server_msg:
        s.send(raw_input('test# '))
    else:
        print server_msg
        server_msg = s.recv(4096)'''
def sending():
    while True:
        client_msg = raw_input('test# ')
        s.send(client_msg)
        print '[+] Client message sent'
    return

def reciving():
    while True:
        server_msg = s.recv(4096)
        if server_msg:print server_msg
    return

threading.Thread(target=reciving).start()
print '\n[+] Thread reciving created\n'
time.sleep(1)
threading.Thread(target=sending).start()
print '\n[+] Thread sending created\n'
time.sleep(10)
s.send(sends)
print '\n[+] Sent the user and pass details'
