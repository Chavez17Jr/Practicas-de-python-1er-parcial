a=1
b=2
c=-15
p=0
m=0
r=0
ra=0.0
d=0.0
x1=0.0
x2=0.0

p= b**2
m= 4*a*c
r=p-m
if r > 0:
    print('Si se puede')
    ra = r**(1/2)
    d = 2*a
    x1 = (-b + ra)/d
    x2 = (-b - ra)/d
    print(f'El valor de x1 es {x1:.2f} y el valor de x2 es {x2:.2f}')
else:
    print('No se puede')


'''a = 1  # Asigna el valor 1 a la variable a / Assign the value 1 to variable a
b = 2  # Asigna el valor 2 a la variable b / Assign the value 2 to variable b
c = -15  # Asigna el valor -15 a la variable c / Assign the value -15 to variable c
p = 0  # Inicializa p en 0 / Initialize p to 0
m = 0  # Inicializa m en 0 / Initialize m to 0
r = 0  # Inicializa r en 0 / Initialize r to 0
ra = 0.0  # Inicializa ra (raíz) en 0.0 / Initialize ra (root) to 0.0
d = 0.0  # Inicializa d (denominador) en 0.0 / Initialize d (denominator) to 0.0
x1 = 0.0  # Inicializa x1 en 0.0 / Initialize x1 to 0.0
x2 = 0.0  # Inicializa x2 en 0.0 / Initialize x2 to 0.0

p = b**2  # Calcula b al cuadrado y lo guarda en p / Calculate b squared and store in p
m = 4 * a * c  # Calcula 4ac y lo guarda en m / Calculate 4ac and store in m
r = p - m  # Calcula el discriminante (b² - 4ac) y lo guarda en r / Calculate the discriminant (b² - 4ac) and store in r

if r > 0:  # Si el discriminante es positivo, hay dos soluciones reales / If the discriminant is positive, there are two real solutions
    print('Si se puede')  # Muestra que la ecuación tiene solución real / Show that the equation has real solution
    ra = r**(1/2)  # Calcula la raíz cuadrada del discriminante / Calculate the square root of the discriminant
    d = 2 * a  # Calcula el denominador 2a / Calculate the denominator 2a
    x1 = (-b + ra) / d  # Calcula la primera solución de la fórmula cuadrática / Calculate the first solution of the quadratic formula
    x2 = (-b - ra) / d  # Calcula la segunda solución de la fórmula cuadrática / Calculate the second solution of the quadratic formula
    print(f'El valor de x1 es {x1:.2f} y el valor de x2 es {x2:.2f}')  # Imprime los valores de x1 y x2 con dos decimales / Print x1 and x2 values with two decimals
else:  # Si el discriminante no es positivo / If the discriminant is not positive
    print('No se puede')  # Muestra que no se puede resolver con soluciones reales / Show that it can't be solved with real solutions
'''