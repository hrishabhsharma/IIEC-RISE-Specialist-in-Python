import socket
import threading
myp = socket.SOCK_DGRAM         #UDP Protocol
afn = socket.AF_INET           #net address family: ipv4
s = socket.socket(afn,myp)

print("\t---------WELCOME TO MY CHAT APPLICATION(UDP)---------")

ip = input("Enter your IP address: ")
port = input("Enter your port number: ")
s.bind( (ip,int(port)) )

friends_ip = input("Enter your friend's IP address: ")
friends_port = input("Enter your friend's port number: ")

def recieve():
	while True:
		x = s.recvfrom(1024)
		clientip = x[1][0]
		data = x[0].decode()
		print(clientip + ":" + data)
  
def send():
	while True:
		print("(you)Linux: ")
		msg = input()
		s.sendto(msg.encode(), (friends_ip,int(friends_port)) )


x1 = threading.Thread(target=send)
x2 = threading.Thread(target=recieve)

x1.start()
x2.start()
