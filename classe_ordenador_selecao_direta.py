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

# teste
lista = [3, 4, 5, 2, 1, 8, 0, 9, 7, 6]
a = Ordenador()
a.selecao_direta(lista)
lista
