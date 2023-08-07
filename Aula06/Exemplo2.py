#criar uma lista de notas 
notas = [6.25, 2,10,9,8.8]

#valor máximo de uma nota
print("Maior valor:",max(notas))


#Valor mínimo de uma  nota da lista
print("Menor valor:",min(notas))

#Quantidade itens na lista de notas
print("Quantidade de notas:",len(notas))

#soma total das notas da lista
print("Soma das notas:",sum(notas))

#Mostrar média das notas:
print(f"Média aritmetica:{sum(notas)/len(notas):.2f}") 

#operador in
print(11 in notas)

#loop for com notas
for i in notas:
    print(i)