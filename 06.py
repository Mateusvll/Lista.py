#Dadas duas strings, s1 e s2. Escreva um programa para criar uma nova string s3 feita
#do primeiro caractere de s1, depois o último caractere de s2, Em seguida, o segundo caractere de s1
#e o penúltimo caractere de s2, e assim por diante. Quaisquer caracteres restantes vão no final do
#resultado.

def mixing(id1, id2):
    
    aux = 0
    str1 = []
    str2 = []
    
    for letter in id1:
        str1.append(letter)
    
    for letter in reversed(id2):
        str2.append(letter)
    
    while aux < len(id2):
        c1 = str1[aux]
        c2 = str2[aux]
        id3 = id3 + c1 + c2
        aux = aux + 1
    
    while aux < len(id1):
        c1 = str1[aux]
        id3 = id3 + c1
        aux = aux + 1

    print(id3)