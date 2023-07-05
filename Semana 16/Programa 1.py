#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 04/07/2023

import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")
mensagem = input("Digite uma mensagem para ser invertida: ")
resultado = cliente.inverter(mensagem)
print("Resultado da inversão: ", resultado)