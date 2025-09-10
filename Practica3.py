

#hacer un programa que lea 10 numeros y almacene en un arreglo


a = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10): 
    a [i] = int(input(f'escribe un numero {i+1}\n'))

for i in a:
    print(i)


'''a = [0,0,0,0,0,0,0,0,0,0]  
# Se crea una lista 'a' con 10 elementos inicializados en 0  
# Creates a list 'a' with 10 elements initialized to 0  

for i in range(0,10):  
    # Bucle for que recorre los números del 0 al 9 (10 iteraciones en total)  
    # For loop that goes from 0 to 9 (10 iterations in total)  
    
    a[i] = int(input(f'escribe un numero {i+1}\n'))  
    # Pide al usuario un número, lo convierte en entero y lo guarda en la posición i de la lista 'a'  
    # Asks the user for a number, converts it to integer, and stores it in position i of list 'a'  
    # El {i+1} muestra el número de entrada (1 al 10 en lugar de 0 al 9)  
    # {i+1} displays the entry number (1 to 10 instead of 0 to 9)  

for i in a:  
    print(i)  
    # Recorre cada elemento de la lista 'a' y lo imprime uno por uno  
    # Iterates over each element of list 'a' and prints it one by one  '''