import socket
s=  socket.socket()

server_ip = input("\n\t\tEnter Server's IP address: ")
server_port = input("\t\tEnter Server's port number: ")

s.connect( (server_ip,int(server_port)) )
print(s.recv(100))
s.send(b"I am a Client")
