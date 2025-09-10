
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
    
     a = input('Escribe un dato')
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