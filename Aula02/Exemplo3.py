#Leia a idade do usuário e informe se ele é maior ou menor de idade

idade = int(input ("Infome a sua idade:"))
if idade<0:
    print("Idade Invalida!!!")
    print("Verifique o Valor Informado")
else:
    if idade>=18:
        print("Você é maior de idade!")
    else:
        print("Você não é maior de idade")    

