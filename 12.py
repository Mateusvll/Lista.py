#Escreva um programa para encontrar a última posição de uma substring “ Emma ” em
#uma determinada string.


print("Escreva uma frase com a palavra Emma.")
string = input()
string_size = len(string)
print("O tamanho da sua String é: ", string_size, "subStrings.")
print("Qual a ultima vez que Emma apareceu na sua String?")
aux = string.rfind("Emma")
print("Na posição", aux)