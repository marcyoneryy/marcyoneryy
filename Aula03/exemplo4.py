#Estrutura de Repetição while
'''
cont = 0
while cont<=10:
    print(cont,end=" ")
    cont = cont+1
print("\nValor final do contador:",cont)
#Contagem de valor iniciando em 50 até 100
cont = 50
while cont<=200:
    print(cont,end=" ")
    cont = cont+1
print("\nValor final do contador:",cont)
#Contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10
cont = 10
while cont<=80:
    print(cont,end=" ")
    cont = cont+10
print("\nValor final do contador:",cont)
#Mostrar a mensagem "Eu tenho  que estudar" 300x
cont= 1
while cont<=300:
    print(cont,"Eu tenho que estudar !!!")
    cont+=1
    '''
''''
# leia um número e mostre a contagem a partir do zero até o número informado
vlr_final = int(input("Informe o valor final:"))
cont = 0
while cont<=vlr_final:
    print(cont,end= " ")
    cont = cont+1
    '''
#Contagem decrecente iniciando em 23 até 0
'''
cont = 23
while cont<=0:
    print(cont,end=" ")
    cont-=1
    print("\n","-"*50)
'''
#leia 2 números e mostre a contagem do intervalo dos valores informados
num1 = int(input("Informe um valor:")) #10
num2 = int(input("Informe outro valor:")) #5

while num1<=num2:
    print(num1)
    num1+= 1
