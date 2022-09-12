#Faça uma função que remova símbolos/pontuações especiais de uma string

palavra = ('m@ateus!')

nova_palavra = ''.join(filter(str.isalnum, palavra))
print(nova_palavra)