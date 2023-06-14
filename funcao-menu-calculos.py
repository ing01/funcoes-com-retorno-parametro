# Algoritmo contendo algumas funções: a) Função para construir um menu de opções para uma calculadora:
# Menu de cálculos: 1.   Número ao quadrado / 2.   Número ao cubo / 3.   Raiz do número / 4.   Raiz cúbica do número / Qual é a opção desejada?

# b) Desenvolva uma função para cada opção de cálculo.
# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da 
# calculadora digitará qualquer valor diferente dos números do menu.

def quadrado (n1):
  quadrado = n1 ** 2
  return quadrado
def cubo (n1):
  cubo = n1 ** 3
  return cubo
def raiz (n1):
  raiz = n1 ** (1/2)
  return raiz
def raiz_cubica (n1):
  raiz_cubica = n1 ** (1/3)
  return raiz_cubica
def main():
    '''Menu de cálculos
1.   Número ao quadrado
2.   Número ao cubo
3.   Raiz do número
4.   Raiz cúbica do número
Qual é a opção desejada?'''
    menu = float(input("Digite uma opção de calculadora: "))
    while menu >= 1 and menu <= 4:
        n1 = float(input("Digite um número para realizar a conta: "))
        if menu == 1:
            totalQ = quadrado(n1)
            print(f'A raiz quadrada de {n1:0.0f} é {totalQ}')
        if menu == 2:
            totalC = cubo(n1)
            print(f'O cubo de {n1:0.0f} é {totalC}')
        if menu == 3:
            totalR = raiz(n1)
            print(f'A raiz de {n1:0.0f} é {totalR}')
        if menu == 4:
            totalRC = raiz_cubica(n1)
            print(f'A raiz cúbica de {n1:0.0f} é {totalRC}')
        menu = float(input("Digite uma opção de calculadora caso deseja continuar ou outro número para sair: "))
main()
