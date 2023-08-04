#1	Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente.
n1 = int(input("digite o valor inicial:"))
n2 = int(input("digite o valor final:"))
cont = n1
while cont<=n2:
    print(cont,end=" ")
    cont -= 1
else:cont = n1
while cont>=n2:
    print(cont,end=" ")
    cont -= 1