# MERGE SORT RECURSIVO

def merge_sort(lista):
    if len(lista <= 1):  # dase da recursão
        return lista

    meior = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])  # chamada recursiva
    lado_direito = merge_sort(lista[meio:])  # chamada recursiva

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:  # base da recursão
        return lado_direito

    if not lado_direito:  # base da recursão
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)  # chamada recursiva

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])  # chamada recursiva
