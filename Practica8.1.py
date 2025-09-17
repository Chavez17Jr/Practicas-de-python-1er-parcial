'''Hacer un programa que introduzca cadenas de caracteres con las siguientes restricciones 
1: las cadenas no deben tener espacios
2: las cadenas solo pueden tener la primera letra mayuscula
3: obligatoriamente deben tener todas las vovales
el program no termina hasta que la lista tenga 5 elementos'''
def vocales(cad):
    ba = False
    be = False
    bi = False
    bo = False
    bu = False
    #for i in cad:
    if 'a' in cad or 'A' in cad:
        ba = True
    if 'e' in cad or 'E' in cad:
        be = True
    if 'i' in cad or 'I' in cad:
        bi = True
    if 'o' in cad or 'O' in cad:
        bo = True
    if 'u' in cad or 'U' in cad:
        bu = True
    if ba == True and be == True and bi == True and bo == True and bu == True:
        lista.append(cad)
        print(lista)

def minusculas(c1):
    cm = 0
    print(c1)
    for i in c1[1:]:    
        if ord(i)>= 97 and ord(i)<=122:
            cm +=1
    if cm == len(c1)-1:
        print (f'la cadena son minusculas excepto la primera{cm}')
        vocales(c1)
    else:
        print('error la cadena no cumple')

def inicio():
    ce = 0
    nc = ""
    c= input('Escribe una cadena \n')
    for i in c:
        if ord(i) != 32:
             ce += 1
    if ce == len(c):
        if c.isalpha():
            #reviso que sean minusculas
            minusculas(c)
        else: 
            for i in c:
                if ord(i)>= 48 and ord(i)<= 57:
                    pass
                else:
                    nc += i
            print(nc)
            minusculas(nc)
    else:
        print('error la cadena no cumple')

lista = []
if __name__=='__main__':
    while(True):
        inicio()
        if len(lista) >=5:
             break



'''def vocales(cad):  # Función que verifica si una cadena contiene todas las vocales / Function that checks if a string contains all vowels
    ba = False     # Bandera para la vocal 'a' / Flag for vowel 'a'
    be = False     # Bandera para la vocal 'e' / Flag for vowel 'e'
    bi = False     # Bandera para la vocal 'i' / Flag for vowel 'i'
    bo = False     # Bandera para la vocal 'o' / Flag for vowel 'o'
    bu = False     # Bandera para la vocal 'u' / Flag for vowel 'u'
    #for i in cad: # Comentado, sin uso / Commented out, not used
    if 'a' in cad or 'A' in cad:  # Verifica si 'a' o 'A' está en la cadena / Checks if 'a' or 'A' is in the string
        ba = True
    if 'e' in cad or 'E' in cad:  # Verifica si 'e' o 'E' está en la cadena / Checks if 'e' or 'E' is in the string
        be = True
    if 'i' in cad or 'I' in cad:  # Verifica si 'i' o 'I' está en la cadena / Checks if 'i' or 'I' is in the string
        bi = True
    if 'o' in cad or 'O' in cad:  # Verifica si 'o' o 'O' está en la cadena / Checks if 'o' or 'O' is in the string
        bo = True
    if 'u' in cad or 'U' in cad:  # Verifica si 'u' o 'U' está en la cadena / Checks if 'u' or 'U' is in the string
        bu = True
    if ba == True and be == True and bi == True and bo == True and bu == True:  # Verifica si todas las vocales están presentes / Checks if all vowels are present
        lista.append(cad)  # Agrega la cadena a la lista si cumple / Adds the string to the list if it qualifies
        print(lista)       # Imprime la lista / Prints the list

def minusculas(c1):  # Función que valida si todos los caracteres excepto el primero son minúsculas / Function that checks if all characters except the first are lowercase
    cm = 0           # Contador de caracteres minúsculas / Counter for lowercase letters
    print(c1)        # Imprime la cadena / Prints the string
    for i in c1[1:]:  # Recorre la cadena desde el segundo carácter / Iterates over the string starting from the second character
        if ord(i)>= 97 and ord(i)<=122:  # Verifica si el carácter está entre 'a' y 'z' / Checks if character is between 'a' and 'z'
            cm +=1                       # Incrementa el contador si es minúscula / Increments counter if lowercase
    if cm == len(c1)-1:  # Verifica si todos excepto el primero son minúsculas / Checks if all but the first are lowercase
        print (f'la cadena son minusculas excepto la primera{cm}')  # Muestra mensaje de éxito / Prints success message
        vocales(c1)  # Llama a la función para verificar vocales / Calls the function to check vowels
    else:
        print('error la cadena no cumple')  # Muestra mensaje de error si no cumple / Shows error message if it doesn't qualify

def inicio():  # Función principal de validación inicial / Main validation function
    ce = 0      # Contador de caracteres distintos a espacio / Counter for non-space characters
    nc = ""     # Nueva cadena sin números / New string without digits
    c= input('Escribe una cadena \n')  # Solicita al usuario una cadena / Prompts user for a string
    for i in c:  # Recorre cada carácter de la cadena / Iterates over each character in the string
        if ord(i) != 32:  # Si el carácter no es un espacio / If the character is not a space
             ce += 1      # Incrementa el contador / Increments the counter
    if ce == len(c):  # Verifica que no haya espacios en la cadena / Checks that there are no spaces in the string
        if c.isalpha():  # Verifica si todos los caracteres son letras / Checks if all characters are letters
            #reviso que sean minusculas / checks if lowercase
            minusculas(c)  # Llama a la función de minúsculas / Calls the lowercase validation function
        else: 
            for i in c:  # Recorre cada carácter de la cadena / Iterates through each character
                if ord(i)>= 48 and ord(i)<= 57:  # Verifica si es un dígito (0–9) / Checks if it is a digit
                    pass  # Ignora los dígitos / Ignores digits
                else:
                    nc += i  # Agrega el carácter a la nueva cadena / Adds character to new string
            print(nc)        # Imprime la nueva cadena sin dígitos / Prints the new string without digits
            minusculas(nc)   # Llama a la función de minúsculas / Calls the lowercase function
    else:
        print('error la cadena no cumple')  # Muestra error si la cadena tiene espacios / Shows error if the string contains spaces

lista = []  # Lista global para almacenar cadenas válidas / Global list to store valid strings

if __name__=='__main__':  # Punto de entrada principal del programa / Main entry point of the program
    while(True):  # Bucle infinito hasta cumplir condición / Infinite loop until condition is met
        inicio()  # Llama a la función principal / Calls the main function
        if len(lista) >=5:  # Si hay 5 o más cadenas válidas, termina / If 5 or more valid strings are collected, exit
             break'''