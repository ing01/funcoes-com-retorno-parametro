# Algoritmo contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.

def multiplicar(n):
  r = n * 2
  return r

def main():
  num = int(input('Informe um valor: '))
  print('O resultado é',multiplicar(num))

main()
