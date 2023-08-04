#Aplicar operadores lógicos com if
#Leia a quantidade de faltas de um aluno e sua média final
qtd_faltas = int(input("Informe a quantidade de faltas:"))
media = float(input("Informe a sua média final:"))
#Condições de reprovação
#qtd de faltas maior que ou média menor do que 7
#analisar condição do aluno somente se o valor das faltas for maior ou igual a zero
if qtd_faltas>=0:    
  if qtd_faltas>8 or media<7:
    print("Aluno Reprovado")  
    if qtd_faltas>8:
        print(f"Aluno Reprovado pela quantidade de faltas:{qtd_faltas}")
    if media<7:
        print(f"Aluno Reprovado por causa da média:{media:2.0f}")
  else:    
    print("Aluno Aprovado")
else:
    print("Valor de faltas invalido")
