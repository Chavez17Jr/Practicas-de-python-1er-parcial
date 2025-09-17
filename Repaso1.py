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



    '''while(True):  # Bucle infinito que se repetirá hasta que el usuario decida salir / Infinite loop that repeats until user chooses to exit
    p = 0.0  # Inicializa el precio base del producto / Initialize base price of the product
    n = ''  # Inicializa el nombre del producto / Initialize product name
    c = 0.0  # Inicializa el precio con IVA / Initialize price with tax (IVA)
    pv = 0.0  # Inicializa el precio final con impuestos adicionales / Initialize final price with additional taxes

    n = input('escribe el nombre de un producto\n')  # Solicita al usuario el nombre del producto / Ask user for product name
    p = float(input('Escribe el precio\n'))  # Solicita al usuario el precio base y lo convierte a float / Ask user for base price and convert to float
    c = p * 1.12  # Calcula el precio con un 12% de IVA / Calculate price with 12% VAT
    pv = c * 1.16  # Calcula el precio final con un 16% adicional (posiblemente otro impuesto) / Final price including extra 16% (possibly another tax)
    print(f'El precio es:{pv:.2f}')  # Muestra el precio final con dos decimales / Display the final price with 2 decimal places

    res = input('deseas otro producto (s/n)\n')  # Pregunta si se desea ingresar otro producto / Ask if another product should be entered
    if res == 'n' or res == 'N':  # Si la respuesta es "n" o "N", termina el bucle / If answer is "n" or "N", break the loop
        break  # Sale del bucle / Exit the loop

p = 0.0  # Reinicia el precio base / Reset base price
n = ''  # Reinicia el nombre del producto / Reset product name
c = 0.0  # Reinicia el precio con IVA / Reset price with tax
pv = 0.0  # Reinicia el precio final / Reset final price

n = input('escribe el nombre de un producto\n')  # Solicita un nuevo nombre de producto / Ask for a new product name
p = float(input('Escribe el precio\n'))  # Solicita un nuevo precio / Ask for a new price
c = p * 1.12  # Calcula el precio con IVA (12%) / Calculate price with 12% VAT
pv = c * 1.16  # Calcula el precio final con impuesto adicional (16%) / Calculate final price with additional 16% tax
print(f'El precio es:{pv:.2f}')  # Muestra el precio final / Display the final price

for i in range(0, 5):  # Bucle que se ejecuta 5 veces / Loop that runs 5 times
    p = 0.0  # Reinicia el precio / Reset price
    n = ''  # Reinicia el nombre / Reset name
    c = 0.0  # Reinicia el precio con IVA / Reset price with VAT
    pv = 0.0  # Reinicia el precio final / Reset final price

    n = input('escribe el nombre de un producto\n')  # Solicita el nombre del producto / Ask for product name
    p = float(input('Escribe el precio\n'))  # Solicita el precio del producto / Ask for product price
    c = p * 1.12  # Calcula el precio con IVA (12%) / Calculate price with 12% VAT
    pv = c * 1.16  # Calcula el precio final con impuesto adicional (16%) / Calculate final price with 16% additional tax
    print(f'El precio es:{pv:.2f}')  # Imprime el precio final / Print the final price
'''