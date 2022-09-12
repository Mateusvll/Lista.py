#Dadas duas strings, s1e s2. Escreva uma função para criar uma nova string s3 anexando
#s2 no meio de s1.

palavra1 = "mateus"
palavra2 = "lopes"
chainsaw = len(palavra1)
part1 = slice(0,len(palavra1)//2)
part2 = slice(len(palavra1)//2, len(palavra1))
palavra3 = palavra1[part1] + palavra2 + palavra1[part2]
print(palavra3)