import pickle, os       
from socket   import *  
from random   import *  
from constRPC import *  

class Server:
  def __init__(self, port=PORT): 
    self.host = '172.31.23.76'                                 
    self.port = port                      
    self.sock = socket()                     
    self.sock.bind((self.host,self.port))     
    self.sock.listen(5)                        
    self.setOfLists = {}                    

  def run(self):
    while True: 
      (conn, addr) = self.sock.accept() 
      data = conn.recv(1024)             
      request = pickle.loads(data)      

      if request[0] == CREATE:                    
        listID = len(self.setOfLists) + 1    
        self.setOfLists[listID] = []         
        conn.send(pickle.dumps(listID))      

      elif request[0] == APPEND:             
        listID = request[2]                  
        data   = request[1]                  
        self.setOfLists[listID].append(data) 
        conn.send(pickle.dumps(OK))          

      elif request[0] == GETVALUE:           
        listID = request[1]                  
        result = self.setOfLists[listID]     
        conn.send(pickle.dumps(result))      

      elif request[0] == STOP:               
        conn.close()                         
        break                                                        
      conn.close()                           