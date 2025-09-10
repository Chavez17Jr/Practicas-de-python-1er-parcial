''' Hacer un programa que lea nombre, edad y sexo de 5 personas, estos elementos
tienen que estar dentro de una lista '''

# Declaraciones publicas
lista = []

def pedirDatos():
    registros = 0
    while registros <= 4:
        nombre = input('Ingresa un nombre: ')
        edad = input('Ingresa la edad: ')
        sexo = input('Que sexo tiene [H] [M] : ')
        lista.append(nombre+', '+edad+' años, sexo '+sexo)
        registros += 1
    print(f'Registros: \n{lista}')
        
pedirDatos()

'''lista = []  
# Lista vacía donde se guardarán los registros ingresados  
# Empty list where the entered records will be stored  

def pedirDatos():  
    # Definición de la función que pedirá los datos al usuario  
    # Function definition that will ask the user for data  

    registros = 0  
    # Contador para limitar el número de registros a ingresar  
    # Counter to limit the number of records to enter  

    while registros <= 4:  
        # Bucle que se repetirá 5 veces (0 a 4)  
        # Loop that will repeat 5 times (0 to 4)  

        nombre = input('Ingresa un nombre: ')  
        # Pide al usuario que ingrese un nombre  
        # Asks the user to enter a name  

        edad = input('Ingresa la edad: ')  
        # Pide al usuario que ingrese la edad  
        # Asks the user to enter the age  

        sexo = input('Que sexo tiene [H] [M] : ')  
        # Pide al usuario que indique el sexo (Hombre o Mujer)  
        # Asks the user to indicate the sex (Male or Female)  

        lista.append(nombre + ', ' + edad + ' años, sexo ' + sexo)  
        # Combina los datos en un solo string y lo agrega a la lista  
        # Combines the data into a single string and appends it to the list  

        registros += 1  
        # Incrementa el contador de registros  
        # Increments the record counter  

    print(f'Registros: \n{lista}')  
    # Muestra todos los registros ingresados  
    # Displays all the entered records  

pedirDatos()  
# Llama a la función para ejecutar la captura de datos  
# Calls the function to execute the data entry  '''