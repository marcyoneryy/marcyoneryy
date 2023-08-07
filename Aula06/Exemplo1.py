#Aula de listas

lista = [2,8,10,4,55,'coxinha',34,'maionese',33]

print(type(lista))
print("Primeiro item da lista:",lista[0])
print("Último item da lista:",lista[8])
print("Último item da lista:",lista[-1])
print("Penúltimo item da lista :",lista[-2])
print("Quantidade de itens da lista:",len(lista))
#print ("Lista  ordendada:",sorted(lista))

#---------------------------------------------------------------
#pc = ["Mouse", "Monitor","HD","Memoria Ram", "Camera"]
lista2 = [6,8,4,11,55,0,3]
print(sorted(lista2))
print(lista2[2:5])
lista2.append(1000)
print(lista2)
lista2.insert(2,5000)
print(lista2)
lista2.extend(lista)
print(lista2)
lista2.pop(5)
print(lista2)
lista2.remove('coxinha')
print(lista2)
