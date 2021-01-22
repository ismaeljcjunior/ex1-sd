import pickle, os      
from socket   import * 
from constRPC import * 

class Client:
  def __init__(self, port):  
    self.host = '172.31.23.76'          
    self.port = port                       
    self.sock = socket()                   
    self.sock.bind((self.host, self.port)) 
    self.sock.listen(2)                    

  def sendTo(self, host, port, data):
    sock = socket()               
    sock.connect((host, port))    
    sock.send(pickle.dumps(data)) 
    sock.close()

  def recvAny(self):
    (conn, addr) = self.sock.accept()
    return conn.recv(1024)