#Instrucciones de entrada y salida
#print() o el print(f)

# print('Hola mundo')
# print(f'Hola mundo {10}')
#Entradas de datos
# input('escribe un numero')#se introducen solo letras
#casting para convertir a valores especificos
# f = 0.0
# f = float(input('Escribe un numero'))
# a = 0
# a = int(input('Escribe un numero'))
# c = 120
# print(str(c))
# v = ''
# v = str(c)
#solo las variables que no se introducen por teclado, se obloga a inicailizarlas

"""Hacer un programa que lea nombre y precio de un producto, el programa
calculara el costo y precio de venta"""
#el costo involucra el 12% y el IVA el 16%
while(True):
    p=0.0
    n= ''
    c=0.0
    pv=0.0

    n = input('escribe el nombre de un producto\n')
    p= float(input('Escribe el precio\n'))
    c = p * 1.12
    pv = c * 1.16
    print(f'El precio es:{pv:.2f}')

    res = input('deseas otro producto (s/n)\n')
    if res == 'n' or res == 'N':
        break

p=0.0
n= ''
c=0.0
pv=0.0

n = input('escribe el nombre de un producto\n')
p= float(input('Escribe el precio\n'))
c = p * 1.12
pv = c * 1.16
print(f'El precio es:{pv:.2f}')


for i in range(0,5):
    p=0.0
    n= ''
    c=0.0
    pv=0.0

    n = input('escribe el nombre de un producto\n')
    p= float(input('Escribe el precio\n'))
    c = p * 1.12
    pv = c * 1.16
    print(f'El precio es:{pv:.2f}') # solo muestra los decimales deseados pv.2f