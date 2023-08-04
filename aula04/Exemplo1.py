'''
#Estrutura de repetição while(Continuação)
#Leia 5 números e mostre a soma de todos os valores informados
cont = 1
soma = 0  #acumulador
while cont<=5:
    num = float(input("Informe um Valor:"))
    soma = soma+num
    cont +=1
    
print ("Esse é o resultado do valor somado:",soma)
'''
'''
#Calcular a soma dos valores do intervalo(fechado) das variáveis a e b (280)
a = 10
b = 25
soma = 0
while a<=b:
    print(a,end=" ")
    soma += a
    a+=1
    
print("\nO Resultado é:",soma)
'''
#Leia 2 valores (inteiros) e mostre a soma do intervalo entre eles
''''
num = int(input("Informe o 1º Valor:")) #1
num2 = int(input("Informe o 2º Valor:")) #3
soma = 0
if num<num2:
 while num<=num2: 
    soma += num
    num +=1
    
 print("O resultado da soma é:",soma)

elif num2<num:
   while num2<=num:
    soma += num2
    num2 +=1
    print("O Resutado é:",soma)
else:
  print("Os Resultados são iguais")  
'''
'''      
#somar 5 valores positivos informados pelo usuário
soma = 0
cont = 1

while cont<=5:
    valor = (float(input("Informe um valor positivo:")))
    if valor<0:
        continue
    soma+= valor
    cont+=1
print(f"o valor somado é{soma}")
'''
'''
#somar 5 valores negativos informados pelo usuário
ac = 0
cont = 1

while cont<=5:
    valor = float(input("Informe o valor negativo:"))
    if valor>=0:
        print("Eu não creio")
        break
    ac += valor
    cont+=1
print(f"O resultado da soma é {ac}")
'''    
#Leia 3 notas e mostre a média,caso seja digitado um valor negativo ou acima de 10 será solicitado um novo valor
nota_media = 0
cont = 1

while cont<=3:
    nota = float(input("Informe as notas do Aluno:"))
    if nota<0 or nota>10:
        continue
    nota_media+=nota
    cont += 1
print(f"A soma das notas informadas é:{nota_media}")
print(f"A média dos valores informados é {nota_media/3:.2f}")
     

