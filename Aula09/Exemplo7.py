#ler nome e e-email e armazenar no arquivos dados3.txt


try:
    txt = open("Aula09/dados3.txt","a+",encoding='uft-8')
    nome = input("Informe o seu nome: ")
    email = input("Informe o e-mail: ")
    txt.write(f"{nome:^15} - {email:^15}\n")
except:
    print("Erro ao digitar os dados :(")    