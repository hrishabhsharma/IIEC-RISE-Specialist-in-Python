import socket
import threading
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


print("\n\t  -----------WELCOME TO MY CHAT APPLICATION------------")
ip = input("\n\t\tEnter your IP address: ")
port = input("\t\tEnter your port number: ")


s.bind( (ip,int(port)) )
s.listen()

def iiecs(cession,addr):
    print(addr)
    cession.send(b"I am a Server")
    data = cession.recv(100)
    print(data)
    

while True:
    csession, addr = s.accept()
    t1 = threading.Thread(target=iiecs, args=(csession, addr))
    t1.start()







