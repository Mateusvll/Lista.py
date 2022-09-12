#Dadas duas strings, s1e s2, escreva um programa para retornar uma nova string feita de
#primeiro, meio e último caracteres de s1 e s2.

palavra1 = 'flamengo'
palavra2 = 'vasco'
tamanho_palavra1 = len(palavra1)
metade_palavra1 = (tamanho_palavra1 // 2)
tamanho_palavra2 = len(palavra2)
metade_palavra2 = (tamanho_palavra2 // 2)
palavra3 = palavra1[0] + palavra2[0] + palavra1[metade_palavra1] + palavra2[metade_palavra2] + palavra1[-1] + palavra2[-1]
print(palavra3)