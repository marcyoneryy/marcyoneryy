'''
#ler dois números e executar a divisão de valores
try:
    n1 = float(input("Informe o numerador: "))
    n2 = float(input("Informe o denominador: "))
    print(f"O resultado da divisão é{n1/n2:.2f}")
except ValueError:
    print("O valor informado está incorreto!!!")

except ZeroDivisionError:
        print("Houve um problema ao executar a divisão")    
'''    
try:
    n1 = float(input("Informe o numerador: "))
    n2 = float(input("Informe o denominador: "))
    print(f"O resultado da divisão é{n1/n2:.2f}")
except:
    print("Não foi possivel realizar a operação")    