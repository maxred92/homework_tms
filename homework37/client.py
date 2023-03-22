import socket		 	 #import socket module

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	 #create a socket object


HOST = 'localhost'     #reading IP Address
PORT = 7777          #reading port number
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.connect((HOST, PORT))                           #connect to server
    print('The IP address of the server is:', HOST)
    print('The port number of the server is:', PORT)

    while(True):
        calculation = input('Enter the calculation(example: 1+1) or Q to quit: ')
        server_sock.sendall(calculation.encode())
        result = server_sock.recv(1024).decode()

        if result == 'Quit':
            print('Closing connection, bye-bye')
            break
        elif result == 'ZeroDivizion':
            print("You can't divide by 0, try again")
        elif result == 'MathError':
            print('There is an error with your math, try again')
        elif result == 'SyntaxError':
            print('There is a syntax error, please try again')
        elif result == 'NameError':
            print('You did not enter an equation, try again')
        else:
            print('The answer is:', result)


