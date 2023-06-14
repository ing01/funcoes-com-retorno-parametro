# Algoritmo contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.

def num(x, y):
  soma = x + y
  return soma

def main():
  x1 = int(input('Insira um número: '))
  y1 = int(input('Insira outro número: '))
  print('A soma dos números é', num(x1, y1))

main()
