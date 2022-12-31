from socket import*
from threading import*
Client = socket(AF_INET,SOCK_STREAM)
HOST = gethostbyname(gethostname())
PORT = 5050
HEADER = 64
DISCONNECTED = 'Disconnect'
Client.connect((HOST,PORT))

def Send_Message(msg:str):
    length = len(msg)
    str_len = str(length).encode()
    send_length = len(str_len)
    str_len+= b' '*(HEADER-send_length)
    Client.send(str_len)
    Client.send(msg.encode())
    if(msg!=DISCONNECTED):
       
        msg_1 = Client.recv(512).decode()
        print(msg_1)


while(True):
    message = eval(input("Enter your message: "))
    Send_Message(message)
    if(message==DISCONNECTED):
        break
        
    

