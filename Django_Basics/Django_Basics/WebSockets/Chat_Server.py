from socket import*
from threading import*
server = socket(AF_INET,SOCK_STREAM)
HOST = gethostbyname(gethostname())
PORT = 5050
HEADER = 64
server.bind((HOST,PORT))
DISCONNECTED = 'Disconnect'
global record 
record= []

def handle_client(conn :socket,addr):
    global record
    while(True):
        info_length = conn.recv(HEADER).decode()
        if(info_length):
            info = conn.recv(int(info_length)).decode()
            record+=[f"{addr}: {info}"]
            print(f"[{addr}]: {info}")
            if(info == DISCONNECTED):
                break
            str =""
            for i in record:
                str+=i
                str+='\n'
            conn.sendall(str.encode())
    conn.close()


def start_server():
    server.listen()
    Connected = True
    while(Connected):
        conn,addr = server.accept()
        thread1 = Thread(target=handle_client,args=(conn,addr))
        thread1.start()
        print("\n")
        print(f"Total numer of active connections: {active_count()-1}")
start_server()
        
