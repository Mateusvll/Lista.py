#Dadas duas listas, l1 e l2, escreva uma função para criar uma terceira lista l3
#escolhendo um elemento de índice ímpar da lista l1 e elementos de índice par da lista l2.

def listas(l1, l2, l3):
    for id1 in l1:
        if (id1 % 2 != 0):
            l3.append(id1)
            if len(l3) != 0:
                break
    
    for id2 in l2:
        if not (id2 % 2 != 0) :
            l3.append(id2)
    
    print(l3)