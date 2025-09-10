'''hacer un programa que lea una cadena y que muestre en pantalla cuantos numeros tiene, cuantas
mayusculas, cuantas minusculas y cuantos espacios'''


def inicio():
    numeros = "0123456789"
    min = 0
    may =0
    c = 0
    e = 0
    cadena = input('escribe un acadena \n')
    for i in cadena:
        if i in numeros:
            print('es numero')
            c += 1
        if i == ' ':
            e += 1
        if ord(i)>= 9 and ord (i)<= 122:
            min +=1
        if ord(i)>=65 and ord(i)<=90:
            may +=1
    print(f'Los numeros son: {c} \n y los espacios: {e} \n y las minusculas: {min} \n y las mayusculas: {may}\n')

if __name__=='__main__':
    inicio()
    

    '''def inicio():  # Define la función principal llamada 'inicio' / Define the main function called 'inicio'
    numeros = "0123456789"  # Cadena que contiene todos los dígitos numéricos / String containing all numeric digits
    min = 0  # Contador para letras minúsculas / Counter for lowercase letters
    may = 0  # Contador para letras mayúsculas / Counter for uppercase letters
    c = 0  # Contador para números / Counter for numbers
    e = 0  # Contador para espacios / Counter for spaces
    cadena = input('escribe un acadena \n')  # Solicita al usuario que escriba una cadena / Prompts the user to enter a string
    for i in cadena:  # Itera sobre cada carácter de la cadena / Iterates over each character in the string
        if i in numeros:  # Verifica si el carácter es un número / Checks if the character is a number
            print('es numero')  # Imprime que es un número / Prints that it is a number
            c += 1  # Incrementa el contador de números / Increments the number counter
        if i == ' ':  # Verifica si el carácter es un espacio / Checks if the character is a space
            e += 1  # Incrementa el contador de espacios / Increments the space counter
        if ord(i) >= 97 and ord(i) <= 122:  # Verifica si el carácter es una letra minúscula (a-z) / Checks if the character is a lowercase letter (a-z)
            min += 1  # Incrementa el contador de minúsculas / Increments the lowercase letter counter
        if ord(i) >= 65 and ord(i) <= 90:  # Verifica si el carácter es una letra mayúscula (A-Z) / Checks if the character is an uppercase letter (A-Z)
            may += 1  # Incrementa el contador de mayúsculas / Increments the uppercase letter counter
    print(f'Los numeros son: {c} \n y los espacios: {e} \n y las minusculas: {min} \n y las mayusculas: {may}\n')  
    # Muestra el total de números, espacios, minúsculas y mayúsculas / Displays the total of numbers, spaces, lowercase, and uppercase letters

if __name__=='__main__':  # Verifica si este archivo es el programa principal que se está ejecutando / Checks if this file is the main program being run
    inicio()  # Llama a la función 'inicio' / Calls the 'inicio' function
'''