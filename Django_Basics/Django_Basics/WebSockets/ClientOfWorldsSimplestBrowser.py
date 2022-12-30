import socket
Client_Server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT = 9000
HOST = 'localhost'
addr = (HOST,PORT)
Client_Server.connect(addr)

def send_message(msg):

    send_message1 = msg.encode()
    
    Client_Server.send(send_message1)

send_message('')
    
