#ler a idade de um funcionario e tratar possíveis números negativos ou valores acima de 130

idade = int(input("Informe a sua Idade:"))

if idade<0 or idade>130:
    raise Exception("Idade invalida,Tente de Novo :)")

else:
    print(f"Sua idade é:{idade} anos")    