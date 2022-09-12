#dada uma string s1, escreva uma função para retornar a soma e a média dos dígitos que
#aparecem na string, ignorando todos os outros caracteres.

def string_calc(id1):
    for n in id1:
        print(n)
        if n.isdigit():
            amount = amount + int(n)
            average = average * int(n)
    print("A soma foi: ", amount)
    print("A média foi: ", average)