import socket
import threading
HEADER = 64
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT = 5050
my_soc = socket.gethostbyname(socket.gethostname())#Gets My Local IP Adrress can type IP Config in CMD
addr = (my_soc,PORT)
server.bind(addr)#Binds my socket to the current address and port number
#HEADER is basically used to specify the length of the message to be received, since we don't know the length of the message yet. Maximum length of the message will the amount that can be represented by 64 bits. If our message length is 5 we have to convert into UTF encoding and then padd out the remaining space with byte representation of blank space
def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr}")
    Connected = True
    while (Connected):
        msg_length = conn.recv(HEADER).decode()
        
        if(msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode()
            if(msg == "Disconnected"):
                Connected = False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {server}")
    while(True):
        conn,addr = server.accept()# Waits for a connection to start. Returns tuple of connection_object and server address
        thread = threading.Thread(target=handle_client,args=(conn,addr))#Tryng to immitate java cause everyone loves java...
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count()-1}")#Total number of connections to my socket
print("[STARTING SERVER]....")
start()

