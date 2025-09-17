
# def validar(a):
#     c = 0
#     d = 0.0
#     try:
#         c = int(a)
#         print('Es un valor numerico, sin decimal')
#     except ValueError:
#         print('No es un valor numerico, sin decimal')

#     try:
#         d = float(a)
#         print('Es un valor numerico, sin decimal')
#     except ValueError:
#         print('No es un valor numerico, sin decimal')


# def leer():
#     # ord Obtiene el ascii del caracter
#     # isalpha para caracteres
#     # isdigit para numeros
#     # try except ValueError
#     a = input('escribe un dato o valor')
#     validar(a)





# if __name__ == '__main__':
#     leer()


'''hacer un programa que lea un dato y que lo almacene en una lista
respetando su tipo de dato'''
def validar(a):
    ne = 0
    try:
        ne = int(a)
        return ne
    except ValueError:
        print('no es un entero')
    try:
        nf = float(a)
        return nf
    except ValueError:
        print('no es numero con decimales')
    return a

def leer():
    
     a = input('Escribe un dato\n')
     dato = validar(a)
     lista.append(dato)
lista = []
if __name__ == '__main__':
    while(True):
        leer()
        res = input('desea continuar s/n')
        if res == 'n' or res == 'N':
            print(lista)
            break


'''def validar(a):  # Define una función para validar el tipo de dato ingresado / Define a function to validate the input data type
    ne = 0  # Inicializa la variable ne en 0 / Initialize variable ne to 0
    try:  # Intenta convertir el dato a entero / Try to convert the input to integer
        ne = int(a)  
        return ne  # Si es entero, lo retorna / If it's an integer, return it
    except ValueError:  # Si ocurre un error al convertir a entero / If error occurs while converting to int
        print('no es un entero')  # Muestra mensaje de error / Show error message

    try:  # Intenta convertir el dato a flotante / Try to convert input to float
        nf = float(a)
        return nf  # Si es número con decimales, lo retorna / If it's a float, return it
    except ValueError:  # Si ocurre un error al convertir a float / If error occurs while converting to float
        print('no es numero con decimales')  # Muestra mensaje de error / Show error message

    return a  # Si no es número, retorna el valor original (probablemente texto) / If not a number, return the original value (likely a string)

def leer():  # Define una función para leer un dato del usuario / Define a function to read input from user
     a = input('Escribe un dato\n')  # Solicita un dato al usuario / Ask user for input
     dato = validar(a)  # Valida el dato usando la función validar / Validate the input using validar function
     lista.append(dato)  # Agrega el dato validado a la lista / Append the validated input to the list

lista = []  # Inicializa una lista vacía para almacenar los datos / Initialize an empty list to store inputs

if __name__ == '__main__':  # Comprueba si el archivo se está ejecutando directamente / Check if the script is being run directly
    while(True):  # Bucle infinito para ingresar varios datos / Infinite loop to allow multiple inputs
        leer()  # Llama a la función leer para obtener y validar un dato / Call leer to get and validate input
        res = input('desea continuar s/n')  # Pregunta al usuario si desea continuar / Ask user if they want to continue
        if res == 'n' or res == 'N':  # Si el usuario responde 'n' o 'N', termina el bucle / If response is 'n' or 'N', break the loop
            print(lista)  # Imprime la lista de datos ingresados / Print the list of entered data
            break  # Sale del bucle / Exit the loop
'''