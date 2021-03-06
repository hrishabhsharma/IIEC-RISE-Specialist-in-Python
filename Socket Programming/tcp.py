import socket
import threading
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("\t---------WELCOME TO MY CHAT APPLICATION(UDP)---------")

ip = input("Enter your IP address: ")
port = input("Enter your port number: ")
s.bind( (ip,int(port)) )
s.listen()

friends_ip = input("Enter your friend's IP address: ")
friends_port = input("Enter your friend's port number: ")

def recieve():
	while True:
		csession, addr = s.accept()
		data = csession.recv(1024)
		print(addr + ":" + data)
  
def send():
	while True:
		s.connect( (friends_ip,int(friends_port)) )
		print("(you)Linux: ")
		msg = input()
		s.send(msg.encode())


x1 = threading.Thread(target=send)
x2 = threading.Thread(target=recieve)

x1.start()
x2.start()
