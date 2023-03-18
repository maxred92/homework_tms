import socket		 	


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	

HOST = 'localhost'     
PORT = 7777


server_sock.bind((HOST,PORT)) 		
server_sock.listen(5) 		     

print('Server is up and running')

while True:
     c, addr = server_sock.accept() 		
     print('Got connection from', addr)

     while True:
          try:
               calculation=c.recv(1024).decode()
               if calculation == 'Q' or calculation == 'q' or calculation == 'Quit' or calculation == 'quit':
                    c.send('Quit'.encode())
                    break
               else:
                    print('You gave me the equation:', calculation)
                    result = eval(calculation)
                    c.send(str(result).encode())
          except (ZeroDivisionError):
               c.send('ZeroDivizion'.encode())
          except (ArithmeticError):
               c.send('MathError'.encode())
          except (SyntaxError):
               c.send('SyntaxError'.encode())
          except (NameError):
               c.send('NameError'.encode())

     c.close() 			