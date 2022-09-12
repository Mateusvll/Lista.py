#Escreva uma função para verificar se duas strings estão balanceadas. Por exemplo, as
#strings s1 e s2 são balanceadas se todos os caracteres em s1 estiverem presentes em s2. A posição
#do caractere não importa


palavra1 = 'Mateus'
palavra2 = 'Suetam'
def compare(palavra1, palavra2):
    test = True
    for aux in palavra1:
        if aux in palavra2:
            continue
        else:
            test = False
    return test