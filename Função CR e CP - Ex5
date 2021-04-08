##Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. 
##Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, 
##ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o 
##que se pagava para todos os funcionário e o que será pago após o aumento.

def porcentagem (porcento, salarios):
    aumento = salarios * (porcento / 100 + 1)
    return aumento
    
def main():
    total_salarios = 0
    porcent = float(input("Digite uma porcentagem de aumento: "))
    for i in range (5):
      salario = float(input("Digite o salário: "))
      total = porcentagem (porcent, salario)
      print(total)
      total_salarios = total_salarios + (total - salario)
      print('O total gasto com o aumentos dos salários é:',total_salarios)
      print(f'O total gasto com o salario {salario} a diferença é: {total - salario}')
      
main()
