try:
    txt  = open("Aula09/dados.txt","r")
    print("Arquivo encontrado :)")
    txt.seek(0)
    print(txt.read())
except:
    print("Problemas ao abrir o arquivo , tente novamente")