import pickle, os      
from socket   import * 
from constRPC import * 

class DBClient:
  def __init__(self, host, port, listID=None):  
    self.host   = host     
    self.port   = port     
    self.listID = listID   

  def sendrecv(self, message):
    sock = socket()                        
    sock.connect((self.host, self.port))   
    sock.send(pickle.dumps(message))       
    result = pickle.loads(sock.recv(1024)) 
    sock.close()                           
    return result

  def create(self):
    assert self.listID == None 
    self.listID = self.sendrecv([CREATE])
    return self.listID
  
  def getValue(self):
    assert self.listID != None 
    return self.sendrecv([GETVALUE, self.listID])
    
  def appendData(self, data):
    assert self.listID != None 
    return self.sendrecv([APPEND, data, self.listID])