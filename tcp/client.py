from socket import *

host = gethostname()
port = 39931

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

while 1:
    msg = input("Digite: ")
    client.send(msg.encode())