#leia um número real e armazene o valor em uma variavel 
num = float (input("Informe um número:"))
print(type(num))

#verificar se o número informado é positivo
if num>0:   #Teste for True
    print("O Valor informado é positivo!")
elif num==0:
    print("o valor informado é neutro")  
else:        #Teste for False
    print("o valor informado é negativo!")

print("Aqui finaliza o script!!!")
