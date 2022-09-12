#Dada uma string que contém uma combinação de letras maiúsculas e minúsculas.
#Escreva uma função para organizar os caracteres de uma string de forma que todas as letras
#minúsculas venham primeiro.

palavra = 'MaTeUs'
id1 = [char for char in palavra if char.islower()]
id2 = [char for char in palavra if char.isupper()]
palavraordenada = ''.join(id1 + id2)
print(palavraordenada)