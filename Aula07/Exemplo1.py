#Trabalhar com estrutrura de dados dicionarios(dict)

dados = {}
print(type(dados))
alunos = {111:"Karla da Silva",222:"Hélio Santos",333:"Manoel Gomes",444:"Bruna Mattos"}

#mostrar primeiro item do dicionário
print(alunos[111])

#mostrar somente as chaves do dicionário
print(alunos.keys())

#mostar somente os valores armazenados no dicionário
print(alunos.values())

#mostrar os itens do dicionário
print(alunos.items())

#atualizar dicionário
alunos.update({555:"Paulo Coelho"})
print(alunos)
alunos[666] = "Teste"
print(alunos)
alunos[111] = "Carlos da Silva"
print(alunos)

#Excluir um item do dicionário
alunos.pop(666)
print(alunos)

#Mostrar somente os valores do dicionário
for i in alunos.values():
    print(i)

#mostrar somente as chaves do dicionário
for i in alunos.keys():
    print(i)

#mostar somente todos os itens do dicionário
for i in alunos.items():
    print(i)

for i,j in alunos.items():
    print(i," - ",j)
    print(i,j,sep=" - ")       

dados = {
    'lista_a':[1,2,2,5,8],
    'lista_b':[10,20,30,40],
    'lista_c':[100,200,300,400]
}
print(dados)
print(type(dados))

#Mostrar o último item da lista b
print(dados["lista_b"][-1])
