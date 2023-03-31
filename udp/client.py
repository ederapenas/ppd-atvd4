from socket import *
import random
import time

def get_random_number(begin_number, number_of_decimal_places):
    random_integer = random.randrange(begin_number, ((10 ** number_of_decimal_places) - 1))
    return random_integer

while True:
    msg_to_send = ""
    msg_received_str = ""

    client = socket(AF_INET, SOCK_DGRAM)

    random_integer_to_send = get_random_number(begin_number=1, number_of_decimal_places= random.randrange(1,30))

    msg_to_send = str(random_integer_to_send)
    print("Numero randomico gerado enviado para o servidor: " + msg_to_send)

    client.sendto(msg_to_send.encode(), ("localhost", 39931))
    msg_received_bytes, address_ip_server = client.recvfrom(2048)
    msg_received_str = msg_received_bytes.decode()
    print("Mensagem recebida do servidor: " + msg_received_str)

    msg_to_send = msg_received_str + "FIM "
    print("Mensagem enviada para o servidor: " + msg_to_send)
    client.sendto(msg_to_send.encode(), ("localhost", 39931))

    client.close()
    for i in range(30):
        print(str(i+1)+ "seg...")
        time.sleep(1)