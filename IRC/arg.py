import argparse
import time
import threading
import socket

parse = argparse.ArgumentParser()
parse.add_argument("--name",help="nick name")
parse.add_argument("--password",help ="password if you are a registerd user, no need to give password")
parse.add_argument("--ircserver",help = "give the IRC server adresses ")
parse.add_argument("--port",help = "specify the port to connect to the irc server")
parse.add_argument("--login",help = "give the login type, if login password give 'yes' and for anonymous login specify 'no'")


args = parse.parse_args()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name = str(args.name)
password= "none"
if (args.login is "yes"):password = args.password
if args.ircserver:
	if args.port:
		sock.connect((socket.gethostbyname(args.ircserver),int(args.port)))
	else:
		sock.connect((socket.gethostbyname(args.ircserver),6667))
else:

	sock.connect((socket.gethostbyname('irc.freenode.com'),6667))

server_msg = sock.recv(4096)
if server_msg:print (server_msg)
def connecting():
		time.sleep(2)
		sock.send('PASS '+password+'\n')
		sock.send('NICK '+name+'\n')
		sock.send('USER none none none none \n')
		return

connecting()

if server_msg:print (server_msg)


def sending():
	while True:
		client_msg = raw_input(args.name+":>>> ")
		client_msg = client_msg+'\n'
		sock.send(client_msg)
		#print ("client msg: "+client_msg+" is sent")
		if "QUIT" in client_msg.lower():
			sock.send("QUIT")
			print ("[+] Quitting From IRC server")
	return

def reciving():
	while True:
		server_msg = sock.recv(4096)
		if server_msg:
                        print(server_msg)
                        if 'PING' in server_msg:sock.send(server_msg)
                        if 'PONG' in server_msg:
                                pong = server_msg.split('PONG')
                                pong_address = pong.split(' ')[-1]
                                sock.send('PONG '+pong_address)
                if 'PRIVMSG' in server_msg:
                       servermsg = server_msg.split('!')
                       name = servermsg[0]
                       #print name
                       message = servermsg[-1].split(':')
                       #print message
                       message = message[-1]
                       print (name+': '+message)
                
	return
#print sock.recv(4096)
threading.Thread(target=reciving).start()
#print ('[+] Threaading of reciving started')
threading.Thread(target=sending).start()
#print ('[+] Threading of sending started')
