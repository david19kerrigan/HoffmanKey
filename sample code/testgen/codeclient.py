# client.py  
import socket
import pickle #saving/loading library

def puzzle(name,params):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # get local machine name
    host = socket.gethostname()                           
    port = 8888
    # connection to hostname on the port.
    s.connect((host, port))                               
    # Receive no more than 1024 bytes
    tm = s.recv(1024).decode('ascii')                 
    print("The server says,{}".format(tm))
    tosend = pickle.dumps([name,params])
    s.sendall(tosend.encode())
    result = pickle.loads(s.recv(1024).decode('ascii'))
    
    s.close
    return result
