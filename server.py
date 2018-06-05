# multi threaded multi socket server to handle requests from developers, and general clients. 

import socket
import sys
from thread import *

host = ''
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try: s.bind((host,port))
except socket.error:
    print("Binding Failed")
    sys.exit
    
s.listen(10)
print("Socket Bound")

def clientthread(conn):
    welcomemessage = "welcome"
    conn.send(welcomemessage.encode())
    
    while True:
        data = conn.recv(1024)
        username += data.decode()
        conn.sendall(data)
        print(username)
    conn.close()
    
    
while 1:
    conn, addr = s.accept() 
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    start_new_thread(clientthread, (conn,))
    
s.close()
    