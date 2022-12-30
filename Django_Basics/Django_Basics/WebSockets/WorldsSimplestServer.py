from socket import*
import threading
server = socket(AF_INET,SOCK_STREAM)
server.bind(('localhost',9000))
        
def handle_client(conn,addr):
    print(addr)
    
    info = conn.recv(5000).decode()
    print(info,len(info))
    
    if(len(info)>1): 
        
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"
        data += "<html><body>Hello World</body></html>\r\n\r\n"
        conn.sendall(data.encode())
        
    conn.shutdown(SHUT_WR)


    
  
   
def start():
    server.listen()
    print(f"Server is listening on {server}")
    while(True):
        conn,addr = server.accept()# Waits for a connection to start. Returns tuple of connection_object and server address
        thread = threading.Thread(target=handle_client,args=(conn,addr))#Tryng to immitate java cause everyone loves java...
        thread.start()
        break
        
start()








