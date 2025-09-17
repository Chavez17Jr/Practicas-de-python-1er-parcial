arr = [0,0,0,0,0,0,0,0,0,0]
car = []
c = 0
c2 = 0
while (True):
    a = input('Escribe un dato o valor: ')
    if a.isdigit():
        arr[c] = int (a)
    elif a.isalpha():
        car.append(a)
    c += 1
    if c > 9:
        break
print (f'La lista tiene {len(car)}')
for i in arr:
    if i != 0:
        c2 += 1
print (f'El arreglo tiene {c2}')
print (arr)


'''arr = [0,0,0,0,0,0,0,0,0,0]  # arreglo (lista) con 10 ceros / array (list) with 10 zeros
car = []  # lista vacía para almacenar caracteres / empty list to store characters
c = 0     # contador para controlar la posición en el arreglo / counter to track position in array
c2 = 0    # contador para contar valores distintos de cero en el arreglo / counter for non-zero values in array

while (True):  # ciclo infinito hasta romper con break / infinite loop until break
    a = input('Escribe un dato o valor: ')  # solicita al usuario un dato / asks user for input
    if a.isdigit():  # si el dato es un número (entero positivo) / if input is a digit (positive integer)
        arr[c] = int(a)  # convierte a entero y lo guarda en la posición correspondiente de arr / convert to int and store in array
    elif a.isalpha():  # si el dato es solo letras / if input is alphabetic
        car.append(a)  # lo añade a la lista de caracteres / adds it to the character list
    c += 1  # incrementa el contador / increments the counter
    if c > 9:  # si ya se ingresaron 10 datos en total / if 10 items have been entered in total
        break  # termina el ciclo / breaks the loop

print (f'La lista tiene {len(car)}')  # muestra cuántos elementos hay en la lista de caracteres / shows how many character elements there are

for i in arr:  # recorre cada elemento en el arreglo / iterates through each item in the array
    if i != 0:  # si el elemento es distinto de cero / if the element is not zero
        c2 += 1  # incrementa contador de elementos válidos / increments the valid element counter

print (f'El arreglo tiene {c2}')  # muestra cuántos números distintos de cero hay / shows how many non-zero numbers are in the array
print (arr)  # imprime el arreglo completo / prints the full array'''