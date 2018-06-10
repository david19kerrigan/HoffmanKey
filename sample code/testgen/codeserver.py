# multi threaded multi socket server to handle requests from developers, and general clients. 
from puzzles import *
import pickle #saving/loading library
import socket
import sys
from thread import *

host = ''
port = 8888

def puzzle(name,params):
    return globals()[name](*params)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try: s.bind((host,port))
except socket.error:
    print("Binding Failed")
    sys.exit
    
s.listen(10)
print("Socket Bound")

def clientthread(conn):
    welcomemessage = "welcome"
    conn.sendall(welcomemessage.encode())
    done = False
    puzzlesolve(conn)
    conn.close()

    
def puzzlesolve(conn):
    inpuzzle = pickle.loads(conn.recv(1024).decode('ascii'))
    outpuzzle = puzzle(*inpuzzle)
    tosend = pickle.dumps(outpuzzle)
    conn.sendall(tosend.encode())
    
    
while 1:
    conn, addr = s.accept() 
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    start_new_thread(clientthread, (conn,))
    
s.close()
    
