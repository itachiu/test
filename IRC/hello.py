import socket

import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((socket.gethostbyname('irc.freenode.com'),6667))

def sending():
    while True:
        s.send(raw_input('test# '))
        s.send('\n')

    return

def reciving():
    while True:
        server_msg = s.recv(4096)
        print server_msg
        if ('PING' in server_msg) or ('PONG' in server_msg):
            new = server_msg.split(':')
            ping_request = new[0]+new[-1]
            print ping_request
            s.send(str(ping_request))
    return

threading.Thread(target=reciving).start()
threading.Thread(target=sending).start()

