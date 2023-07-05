#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 04/07/2023

from xmlrpc.server import SimpleXMLRPCServer

def somar_numeros(a, b):
    return a + b

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(somar_numeros, "somar")
print("Servidor de soma iniciado.")
server.serve_forever()