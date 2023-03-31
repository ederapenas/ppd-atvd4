from socket import *

host = gethostname()
port = 39931

print(f'HOST: {host}, PORT: {port}')

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(5)

while(1):
    con, adr = server.accept()
    while(1):
        msg = con.recv(1024)
        print(msg.decode())