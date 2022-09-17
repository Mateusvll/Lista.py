#Implemente uma função que encontre a interseção (elementos comuns) de dois
#conjuntos (set) e remova esses elementos do primeiro conjunto.

def intsec_sets(x, y):    
    x = {81, 19, 20, 22}
    y = {20, 40, 60}
    z = x.difference(y)
    x = z
    
    print(x)