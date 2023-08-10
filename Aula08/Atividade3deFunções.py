#Crie uma função em Python para mostrar o produto da multiplicação entre n valores.
def mult_valores(*args):
    aux = 1
    for i in args:
        aux*= i
    return aux
print(mult_valores(4,4,4,4))