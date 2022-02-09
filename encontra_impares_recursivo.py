'''
Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista
de números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
'''


def encontra_impares(lista):
    listaimp = []
    if len(lista) > 0:
        numero = lista.pop(0)
        if numero % 2 != 0:
            listaimp.extend([numero])
        listaimp = listaimp + encontra_impares(lista)
    return listaimp

# teste
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(encontra_impares(a))
