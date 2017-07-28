import socket
import socks

server = "YOURSERVER" #CHANGETHIS
channel = "#CHANNEL" #CHANGETHIS
botnick = "YOURBOTNICK" #CHANGETHIS

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("connecting to:"+server)
socket.connect((server, 6667))
socket.send(("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun   bot!\n").encode())
socket.send(("NICK "+ botnick +"\n").encode())
socket.send(("PRIVMSG nickserv :iNOOPE\r\n").encode())

while 1:
	text=socket.recv(2040)
	print (text)
	text=str(text)

	if text.find('PING') != -1:
		socket.send(('PONG ' + text.split() [1] + '\r\n').encode())
		socket.send(("JOIN "+ channel +"\n").encode())