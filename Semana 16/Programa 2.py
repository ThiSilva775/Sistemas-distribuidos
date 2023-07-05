#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 04/07/2023

from xmlrpc.server import SimpleXMLRPCServer

def inverter_string(string):
    return string[::-1]

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(inverter_string, "inverter")
print("Servidor de inversão de string iniciado.")
server.serve_forever()