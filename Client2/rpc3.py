import pickle, os              
from socket   import *         
from time     import sleep     
from random   import *        
from constRPC import *         

from client   import *         
from server   import *         
from dbclient import *         


sleep(1) 
pid = os.fork()
if pid == 0:
      print(f"Realizando conexão com o {HOSTCL2} na porta {CLIENT2}")
      client2 = Client(CLIENT2)				
      
      print(f"Aguardando até que os dados sejam enviados")
      data = client2.recvAny()				
      
      print(f"Recebendo a referencia remota")
      dbClient2 = pickle.loads(data)				
      
      print("Concatenando o Cliente 2 ")
      dbClient2.appendData('Cliente 2')			 
      
      sleep(5)
      
      print (f"Dados: {dbClient2.getValue()}")
      print(f"Enviando os dados para o {HOST} na porta {PORT}")
      client2.sendTo(HOST,PORT,[STOP])
      print(f"Finalizando...")
      os._exit(0)
