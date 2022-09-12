#Crie uma função que encontre todas as ocorrências de uma substring em uma
#determinada string ignorando o caso.

def counter(str, subStr):

    count = str.count(subStr)

    print("Quantidade de sub-strings na string foi: ", count)