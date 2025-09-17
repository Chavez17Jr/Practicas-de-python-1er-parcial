a = [10] # arreglo 
b = [] #lista

a[0] = 10
a[0] = 10

b = ('hola', 10,10.05, False, 'm', {1,2,3,4})

#ciclos y condiciones
if (len(a) > len(b)):
    print('A es mayor')
else:
    print('B es mayor')

for i in a:
    print(a)



'''a = [10]  # arreglo (lista con un solo elemento) / array (list with one element)
b = []    # lista vacía / empty list

a[0] = 10  # asigna el valor 10 a la posición 0 (sin cambio real) / assigns 10 to index 0 (no real change)
a[0] = 10  # asigna nuevamente el valor 10 (redundante) / assigns 10 again (redundant)

b = ('hola', 10, 10.05, False, 'm', {1,2,3,4})  
# b ahora es una tupla con varios tipos de datos / b is now a tuple with various data types

# ciclos y condiciones / loops and conditions
if (len(a) > len(b)):  # compara las longitudes de a y b / compares lengths of a and b
    print('A es mayor')  # imprime si 'a' es más larga / prints if 'a' is longer
else:
    print('B es mayor')  # imprime si 'b' es más larga / prints if 'b' is longer

for i in a:  # recorre cada elemento en la lista 'a' / iterates over each element in list 'a'
    print(a)  # imprime toda la lista 'a' en cada iteración / prints the entire list 'a' on each iteration
'''