# Algoritmo contendo algumas funções: a) Função para construir um menu de opções para uma calculadora:
# Minha Calculadora: Digite um número; Digite outro número; + Soma dois números; - Subtrai dois números; * Multiplica dois números; / Divide dois números; Qual opção deseja? 
# b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.
# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará 
# qualquer valor diferente dos caracteres do menu.

def soma (n1, n2):
    soma = n1 + n2
    print(f'A soma de {n1:0.0f} + {n2:0.0f} é {soma:0.0f}')
def subtrai (n1, n2):
    subtrai = n1 - n2
    print(f'A subtração de {n1:0.0f} - {n2:0.0f} é {subtrai:0.0f}')
def multiplica (n1, n2):
    multiplica = n1 * n2
    print(f'A multiplicação de {n1:0.0f} * {n2:0.0f} é {multiplica:0.0f}')
def divide (n1, n2):
    divide = n1 / n2
    print(f'A divisão de {n1:0.0f} / {n2:0.0f} é {divide:0.0f}')
def main():
    '''Minha calculadora
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual é a opção desejada?'''
    menu = str(input("Digite uma opção de calculadora: "))
    while menu == '+' or menu == '-' or menu == '*' or menu == '/':
        n1 = float(input('Digite um número para realizar a conta: '))
        n2 = float(input('Digite outro número para realiza a conta: '))
        if menu == '+':
          soma (n1, n2)
        if menu == '-':
          subtrai (n1, n2)
        if menu == '*':
          multiplica (n1, n2)
        if menu == '/':
          divide (n1, n2)
        menu = float(input("Digite uma opção de calculadora caso deseja continuar ou outro caracter para sair: "))
main()
