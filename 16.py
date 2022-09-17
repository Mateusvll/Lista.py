#Faça uma função que remova de todos os caracteres de uma string, exceto números
#inteiros

palavra = "o Flamengo tem 3 copas do brasil, 8 brasileiros e 2 libertadores"
resultado = ''.join(filter(lambda aux: aux if aux.isdigit() else None, palavra))
print(resultado)