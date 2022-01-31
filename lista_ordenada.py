# Coursera Curso Python Nível 2
# Lista ordenada

'''
Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com
números inteiros como parâmetro e devolve o booleano True
se a lista estiver ordenada e False se a lista não
estiver ordenada.
'''

def ordenada(lista):
    menor_item =  lista[0]
    flag = True
    while flag:  
      for idx in range(len(lista)):
        if lista[idx] > menor_item:
          menor_item = lista[idx]
        else:
          flag = False
          if idx == len(lista)-1:
            return False
      return True


# testes
a = [55, 33, 0, 900, -432, 10, 77, 2, 11]
print(ordenada(a))

b = [-432, 0, 2, 10, 11, 33, 55, 77, 900]
print(ordenada(b))

c = [-3, 30, 45, 87, 90, 122, 234, 500]
print(ordenada(c))

d = [500, 45, 90, 30, 87, 122, -3, 234]
print(ordenada(d))

e = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(ordenada(e))

f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(ordenada(f))

