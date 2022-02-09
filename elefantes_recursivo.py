'''
Exercício 3: Elefantes
Este exercício tem duas partes:

1 - Implemente a função incomodam(n) que devolve uma string contendo "incomodam "
(a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente
positivo, a função deve devolver uma string vazia. Essa função deve ser implementada
utilizando recursão.

2 - Utilizando a função acima, implemente a função elefantes(n) que devolve uma
string contendo a letra da música "Um elefante incomoda muita gente" de 1 até
n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia.
Essa função também deve ser implementada utilizando recursão.

Observe que, para um elefante, você deve escrever por extenso e no singular
("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+".
Lembre-se também que é possível transformar números em strings com a função str().

Dica: Será que neste caso a base da recursão é diferente de  n == 1 n==1?
'''

def elefantes(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente"
    elif n == 2:
        return elefantes(n-1) + f"\n{n} elefantes "+ incomodam(n) +"muito mais"
    else:
        frasepri = f"\n{n-1} elefantes incomodam muita gente"
        fraseseg = f"\n{n} elefantes "+ incomodam(n) +"muito mais"
        return elefantes(n-1) + frasepri + fraseseg

def incomodam(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n - 1)

# teste
print(elefantes(4))