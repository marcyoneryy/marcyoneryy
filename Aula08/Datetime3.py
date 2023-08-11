#Mostrar dia da semana, data e hora
import datetime


x = datetime.datetime.now()
print(x.strftime("%A")," - ",x)