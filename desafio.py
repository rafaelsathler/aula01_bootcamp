nome = input("Digite o seu nome: ")

salario = float(input("Digite o valor do seu salário: "))

bonus = float(input("Digite o seu bônus: "))

kpi = 1000 + salario * bonus

print(kpi)

print(f"O salário do {nome} é de {salario} com bônus de {bonus}, totalizando no final {kpi}")