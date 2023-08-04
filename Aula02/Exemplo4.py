#leia dois números inteiros e mostre somente o menor valor
num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))
if num1<num2: 
    print("o menor valor é:",num1)
elif num1==num2:
    print("Você digitou valores iguais! :(")    
else:
    print("o menor valor é:",num2)    
