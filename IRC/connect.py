from socket import *
import time
s = socket(AF_INET,SOCK_STREAM)

s.connect((gethostbyname('irc.freenode.com'),6667))
print s.recv(4096)
time.sleep(3)
s.send('PASS none')
s.send('NICK test007')
s.send('USER bla bla bla bla')
server_msg = s.recv(4096)
while True:
    if 'not enough parameters' in server_msg.lower():
        s.send('PASS none')
        s.send('NICK test007')
        s.send('USER bla bla bla bla')
    elif "Couldn't lookup your host name" in server_msg:
        s.send('PASS none')
        s.send('NICK test007')
        s.send('USER bla bla bla bla')
    elif 'Looking up your' in server_msg:
        s.send('PASS none')
        time.sleep(0.5)
        s.send('NICK test007')
        time.sleep(0.5)
        s.send('USER bla bla bla bla')

    else:break
print server_msg
def client_msg():
    command = raw_input('test007# ')
    return command
while True:

    server_msg = s.recv(4096)
    if not server_msg:
        s.send(client_msg())
    if ('PING ') in server_msg or ('PONG ' in server_msg):
        print server_msg
        s.send(server_msg)
    elif (' MODE' in server_msg):
        print '[+] Entered the server'

    s.send(client_msg())

