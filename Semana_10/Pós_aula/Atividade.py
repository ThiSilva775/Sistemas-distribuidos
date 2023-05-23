#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 19/04/2023

import threading

vetor = list(range(1, 101))  # criando um vetor de 1 a 100
soma_total = 0  # inicializando a variável que irá armazenar a soma total

def soma_parte_vetor(inicio, fim):
    global soma_total
    soma = sum(vetor[inicio:fim])  # realizando a soma dos elementos da parte do vetor
    print(f"Soma da parte do vetor de {inicio+1} a {fim}: {soma}")  # imprimindo o resultado da soma da parte
    soma_total += soma  # somando a parte ao resultado total

# criando as threads para realizar a soma das partes do vetor
t1 = threading.Thread(target=soma_parte_vetor, args=(0, 25))
t2 = threading.Thread(target=soma_parte_vetor, args=(25, 50))
t3 = threading.Thread(target=soma_parte_vetor, args=(50, 75))
t4 = threading.Thread(target=soma_parte_vetor, args=(75, 100))

# iniciando as threads
t1.start()
t2.start()
t3.start()
t4.start()

# aguardando as threads terminarem
t1.join()
t2.join()
t3.join()
t4.join()

print(f"Soma total do vetor: {soma_total}")  # imprimindo o resultado da soma total