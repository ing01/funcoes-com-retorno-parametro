# Algoritmo contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou 
# reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.

def notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def calculo (media):
    if media >= 6:
        return str('Aprovado.')
    else:
        return str('Reprovado.')

def main ():
  n1 = int(input('Digite a primeira nota: '))
  n2 = int(input('Digite a segunda nota: '))
  total = notas(n1, n2)
  print(f'{total}')
  aprov_reprov = calculo(total)
  print(f'{aprov_reprov}')

main()
