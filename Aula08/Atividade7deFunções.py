#Crie uma função em Python para retornar a quantidade de itens existentes em um dicionário.
def Mostra_chave(**kwargs):    
    chaves = kwargs
 
    print(f"Aqui é o tamanho do Dicionário: {len(chaves)}")
 
    return chaves
print(Mostra_chave(valor1=777, valor2=272, valor3= 933, valor4 = 424))