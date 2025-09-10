# Declaraciones publicas o globales
arr = [0,0,0,0,0,0,0,0,0,0]
car = []

def resultados(): # Definicion para mostrar los resultados
    c2 = 0
    print (f'La lista tiene {len(car)}')
    for i in arr:
        if i != 0:
            c2 += 1
    print (f'El arreglo tiene {c2}')
    print (car)
    print (arr)

def hola(): # Definicion de metodo o funcion
    c = 0
    while (True):
        a = input('Escribe un dato o valor: ')
        if a.isdigit():
            arr[c] = int (a)
        elif a.isalpha():
            car.append(a)
        c += 1
        if c > 9:
            break
    resultados()


if __name__== "__main__": # Metodo principal
    hola()


'''arr = [0,0,0,0,0,0,0,0,0,0]  
# Lista de tamaño 10 inicializada en ceros, se usará para guardar números  
# List of size 10 initialized with zeros, used to store numbers  

car = []  
# Lista vacía para guardar caracteres (letras) ingresados  
# Empty list to store entered characters (letters)  

def resultados():  # Definición de función para mostrar los resultados  
    # Function definition to display the results  

    c2 = 0  
    # Contador para los elementos diferentes de 0 en 'arr'  
    # Counter for non-zero elements in 'arr'  

    print(f'La lista tiene {len(car)}')  
    # Muestra cuántos elementos tiene la lista 'car'  
    # Displays how many elements the list 'car' has  

    for i in arr:  
        if i != 0:  
            c2 += 1  
            # Cuenta cuántos números se ingresaron en 'arr' (diferentes de 0)  
            # Counts how many numbers were entered in 'arr' (not equal to 0)  

    print(f'El arreglo tiene {c2}')  
    # Imprime cuántos números válidos hay en 'arr'  
    # Prints how many valid numbers are in 'arr'  

    print(car)  
    # Imprime la lista de caracteres ingresados  
    # Prints the list of entered characters  

    print(arr)  
    # Imprime la lista de números (con ceros en las posiciones no usadas)  
    # Prints the list of numbers (with zeros in unused positions)  


def hola():  # Definición de método o función  
    # Definition of method or function  

    c = 0  
    # Contador para recorrer las posiciones de 'arr'  
    # Counter to iterate over positions of 'arr'  

    while (True):  
        # Bucle infinito hasta que se cumpla la condición de salida  
        # Infinite loop until exit condition is met  

        a = input('Escribe un dato o valor: ')  
        # Pide al usuario ingresar un valor (número o letra)  
        # Asks the user to enter a value (number or letter)  

        if a.isdigit():  
            arr[c] = int(a)  
            # Si es un número, lo convierte a entero y lo guarda en 'arr' en la posición c  
            # If it's a number, converts it to integer and stores it in 'arr' at position c  

        elif a.isalpha():  
            car.append(a)  
            # Si es una letra, la agrega a la lista 'car'  
            # If it's a letter, appends it to the list 'car'  

        c += 1  
        # Avanza al siguiente índice del arreglo 'arr'  
        # Moves to the next index of 'arr'  

        if c > 9:  
            break  
            # Si ya se llenaron las 10 posiciones, rompe el ciclo  
            # If all 10 positions are filled, breaks the loop  

    resultados()  
    # Llama a la función resultados() para mostrar lo capturado  
    # Calls resultados() function to display what was captured  


if __name__ == "__main__":  # Método principal  
    # Main method (runs only if this file is executed directly)  

    hola()  
    # Llama a la función principal que pide datos y luego muestra resultados  
    # Calls the main function that asks for data and then shows results '''