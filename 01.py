#Escreva uma função para criar uma nova string feita do primeiro, do meio e do último
#caractere de uma string de entrada.

word = 'palavra'
word_size = len(word)
half_the_word = (word_size//2)
new_word = word[0] + word[half_the_word] + word[-1]
print("\nprimeira letra, letra do meio e ultima letra:", new_word)