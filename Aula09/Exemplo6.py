#Abertura de um arquivo chamado dados2.txt
#ler o nome de uma pessoa

try:

            txt = open("Aula09/dados2.txt","w+")
            for i in range(1,11):
              nome_pessoa = input("Digite seu nome:")
              txt.write(f"{i} - Nome:{nome_pessoa}\n")

except:
    print("Não foi possivel encontar o arquivo")  

else:
    txt.seek(0)
    print(txt.read())
    txt.close() 
       