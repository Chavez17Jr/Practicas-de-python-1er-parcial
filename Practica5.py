

'''hacer un programa que lea 10 datos, si el dato es un numero se almecenara en unarreglo
si es un caracter o caracteres se metera a una lista, cuando finalize el programa nos mostrara
cuantos elementos hay en cada estructura'''
 
numeros = 0
a = []
b = []
x = 0
while(x <= 9):
    c = input('Escribe un caracter \n')
    if c.isdigit():
        a.append(int(c))
        x += 1
    elif c.isalpha():
        b.append(c)
        x +=1
    else:
        print('No es valido')
for i in a:
    numeros +=i
print(f'Letras ingresadas{b}')
print(f'Numeros ingresadas{a}')
print(f'Suma de los carcteres ingresados es: {numeros}')

'''numeros = 0  
# Variable acumuladora para la suma de los números ingresados  
# Accumulator variable for the sum of the entered numbers  

a = []  
# Lista vacía donde se guardarán los números ingresados  
# Empty list where entered numbers will be stored  

b = []  
# Lista vacía donde se guardarán las letras ingresadas  
# Empty list where entered letters will be stored  

x = 0  
# Contador para llevar el control de cuántos caracteres válidos se han ingresado  
# Counter to keep track of how many valid characters have been entered  

while(x <= 9):  
    # Bucle que se repetirá hasta que se ingresen 10 caracteres válidos  
    # Loop that repeats until 10 valid characters are entered  

    c = input('Escribe un caracter \n')  
    # Pide al usuario que escriba un carácter  
    # Asks the user to enter a character  

    if c.isdigit():  
        # Si el carácter ingresado es un número (0-9)...  
        # If the entered character is a digit (0-9)...  

        a.append(int(c))  
        # Convierte el carácter a entero y lo guarda en la lista 'a'  
        # Converts the character to integer and stores it in list 'a'  

        x += 1  
        # Incrementa el contador de caracteres válidos  
        # Increments the counter of valid characters  

    elif c.isalpha():  
        # Si el carácter ingresado es una letra (a-z, A-Z)...  
        # If the entered character is a letter (a-z, A-Z)...  

        b.append(c)  
        # Agrega la letra a la lista 'b'  
        # Appends the letter to list 'b'  

        x += 1  
        # Incrementa el contador de caracteres válidos  
        # Increments the counter of valid characters  

    else:  
        print('No es valido')  
        # Si el carácter no es número ni letra, muestra un mensaje de error  
        # If the character is neither number nor letter, shows an error message  

for i in a:  
    numeros += i  
    # Recorre la lista de números y los suma en 'numeros'  
    # Iterates through the list of numbers and sums them into 'numeros'  

print(f'Letras ingresadas {b}')  
# Imprime la lista de letras ingresadas  
# Prints the list of entered letters  

print(f'Numeros ingresados {a}')  
# Imprime la lista de números ingresados  
# Prints the list of entered numbers  

print(f'Suma de los caracteres ingresados es: {numeros}')  
# Imprime la suma de los números ingresados  
# Prints the sum of the entered numbers  '''