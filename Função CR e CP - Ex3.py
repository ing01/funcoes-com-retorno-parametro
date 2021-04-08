##Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, 
##retorne e apresente o novo salário.

def percent(valor):
  salario = int(input('Insira o valor do salário: '))
  aumento = salario * (valor / 100 + 1)
  print('O salário reajustado é', aumento)
  return aumento

def main():
  porcentagem = int(input('Insira a porcentagem de aumento do salário: '))
  percent(porcentagem)

main()
