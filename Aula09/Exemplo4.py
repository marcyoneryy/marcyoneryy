#mostrar execeção ao digitar números negativos

n = float(input("Informe o valor positivo;"))
if n<0:
    raise ValueError("Número negativo =(")