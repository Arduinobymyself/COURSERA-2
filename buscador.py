'''
Curso de Python do Coursera
Classe que faz buscas em listas
busca sequencia e busca binária
deve ser salvom com o nome buscador.py
'''


import random
import time


class Buscador:
  def busca_sequencial(self, lista, x):
    for i in range(len(lista)):
      if lista[i] == x:
        return i
    return -1

  def busca_binaria(self, lista, x):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
      meio = (primeiro + ultimo) // 2
      if lista[meio] == x:
        return meio
      else:
        if x < lista[meio]:
          ultimo = meio - 1
        else:
          primeiro = meio + 1
    return -1


# testes
lista1 = [x for x in range(40000000)]  # gera uma lista ordenada
lista2 = [random.randrange(4000000)]  #gera uma lista aleatória
# print(lista)

b = Buscador()

inicio = time.time()
print(b.busca_binaria(lista1, 32322055))
print(b.busca_binaria(lista1, 31334567))
print(b.busca_binaria(lista1, 30013302))
fim = time.time()
print(f'Binária em {(fim - inicio):.12f} segundos')

inicio = time.time()
print(b.busca_sequencial(lista1, 32322055))
print(b.busca_sequencial(lista1, 31334567))
print(b.busca_sequencial(lista1, 30013302))
fim = time.time()
print(f'Sequencial em {(fim - inicio):.12f} segundos')
