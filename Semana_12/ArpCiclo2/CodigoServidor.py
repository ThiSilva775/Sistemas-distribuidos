#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 23/05/2023

import socket

# Define o endereço de host e a porta do servidor
HOST = '127.0.0.1'
PORT = 12345

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Liga o socket a um endereço e porta
    server_socket.bind((HOST, PORT))

    # Define o número máximo de conexões em fila
    server_socket.listen(5)

    # Laço principal do servidor
    while True:
        # Aceita uma nova conexão de cliente
        client_socket, client_address = server_socket.accept()

        # Recebe a mensagem do cliente
        message = client_socket.recv(1024).decode('utf-8')

        # Processa a mensagem do cliente
        message_parts = message.split(':')
        message_type = message_parts[0]
        message_body = message_parts[1]

        # Envia uma resposta ao cliente
        response_message = 'Hello, client!'
        client_socket.sendall(response_message.encode('utf-8'))

        # Fecha a conexão com o cliente
        client_socket.close()

# O socket do servidor é fechado automaticamente pelo bloco "with"