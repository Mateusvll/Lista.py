#Escreva uma função para dividir uma determinada string em hífens e exibir cada
#substring.


print("Escreva uma frase:")

def divide_string(words):
    word_list = words.split(' ')
    return word_list

def link_string(word_list):
    words = '-'.join(word_list)
    return words

if __name__ == '__main__':
    words = input()

    string = divide_string(words)

    new_string = link_string(string)
    print(new_string)

for words in string:
    print(words)