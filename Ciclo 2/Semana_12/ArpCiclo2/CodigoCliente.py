#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 23/05/2023

import socket

# Define o endereço de host e a porta do servidor
HOST = '127.0.0.1'
PORT =12345

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Conecta o socket a um endereço e porta
    client_socket.connect((HOST, PORT))

    # Envia uma mensagem de exemplo ao servidor
    message = 'SEND_MESSAGE:alice:Hello, Alice!'
    client_socket.sendall(message.encode('utf-8'))

    # Recebe a resposta do servidor
    response = client_socket.recv(1024).decode('utf-8')

    # Processa a resposta do servidor
    response_parts = response.split(':')
    response_type = response_parts[0]
    response_body = response_parts[1]

# O socket do cliente é fechado automaticamente pelo bloco "with"