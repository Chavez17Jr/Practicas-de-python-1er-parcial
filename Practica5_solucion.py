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