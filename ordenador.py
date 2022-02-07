'''
Esta é a classe principal de Ordenadores do
curso de Python da Coursera-2
deve ser salvo como ordenador.py
'''

class Ordenador:
  def selecao_direta(self, lista):
    fim = len(lista)
    for i in range(fim - 1):
      # inicialmente, o menor elemento já visto é o i-ésimo
      posicao_menor = i
      for j in range(i + 1, fim):
        if lista[j] < lista[posicao_menor]:
          posicao_menor = j
      # coloca o menor elemento encontrado no início da sub-lista
      # para isso, troca de lugar os elementos nas posições i e posicao_menor
      lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]
    return lista


  def bolha(self, lista):
    fim = len(lista)
    for i in range(fim-1, 0, -1):
      for j in range(0, i):
        if lista[j] > lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]


  def bolha_melhorada(self, lista):
    fim = len(lista)
    for i in range(fim-1, 0, -1):
      trocou = False
      for j in range(0, i):
        if lista[j] > lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]
          trocou = True
      if not trocou:
        return
