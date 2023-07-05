#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Thiago Silva Soares
#DATA: 23/05/2023

from threading import Thread

def crescente():
    for i in range(1,501):
        print(f'thread 1 :{i}\n')


def decrescente():
    for j in range(500, 0, -1):
        print(f'thread 2 :{j}\n')

if __name__ == '__main__':

    t1=Thread(target= crescente)
    t2=Thread(target= decrescente)

t1.start()
t1.join()

t2.start()
t2.join()