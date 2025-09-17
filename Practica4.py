#hacer un programa que lea 10 numeros y almacene en una lista
a = []
s = 0
n = 0
numeros = "0123456789"
while ( n < 10):
    b = input ('Escribe un nuemro \n')
    x = 0
    for i in b:
        #if(ord(i) >= 48 and ord(i) <= 57):
        if i in numeros:
           x+=1
    if len(b)==x:
        a.append(int(b))
        n += 1
    else:
        print('El valor no es un numero')
for i in a:
    print (i)
    s += i
print (f'La suma es {s}')

'''a = []  
# Lista vacía donde se guardarán los números ingresados  
# Empty list where the entered numbers will be stored  

s = 0  
# Variable acumuladora que sumará todos los números  
# Accumulator variable that will sum all numbers  

n = 0  
# Contador de cuántos números válidos se han ingresado  
# Counter for how many valid numbers have been entered  

numeros = "0123456789"  
# Cadena que contiene los caracteres válidos para dígitos numéricos  
# String containing the valid characters for numeric digits  

while (n < 10):  
    # Bucle que se repite hasta que se ingresen 10 números válidos  
    # Loop repeats until 10 valid numbers are entered  

    b = input('Escribe un numero \n')  
    # Pide al usuario que ingrese un valor (como texto)  
    # Asks the user to enter a value (as text)  

    x = 0  
    # Contador para verificar cuántos caracteres de la entrada son números  
    # Counter to check how many characters of the input are numbers  

    for i in b:  
        # Recorre cada carácter de la entrada  
        # Iterates through each character of the input  

        # if(ord(i) >= 48 and ord(i) <= 57):  
        # Forma alternativa con ASCII (comentada) para validar si es un número  
        # Alternative with ASCII (commented) to validate if it's a number  

        if i in numeros:  
            x += 1  
            # Si el carácter está en la cadena "0123456789", suma 1 al contador  
            # If the character is in the string "0123456789", add 1 to counter  

    if len(b) == x:  
        # Si todos los caracteres de la entrada son números...  
        # If all characters of the input are numbers...  

        a.append(int(b))  
        # Convierte la entrada a entero y la guarda en la lista 'a'  
        # Converts the input to integer and saves it into list 'a'  

        n += 1  
        # Aumenta el contador de números válidos  
        # Increases the counter of valid numbers  

    else:  
        print('El valor no es un numero')  
        # Si la entrada contiene caracteres no numéricos, muestra error  
        # If the input contains non-numeric characters, show error  

for i in a:  
    print(i)  
    # Recorre la lista 'a' e imprime cada número ingresado  
    # Iterates through list 'a' and prints each entered number  

    s += i  
    # Suma cada número al acumulador 's'  
    # Adds each number to accumulator 's'  

print(f'La suma es {s}')  
# Imprime la suma total de todos los números ingresados  
# Prints the total sum of all entered numbers  '''