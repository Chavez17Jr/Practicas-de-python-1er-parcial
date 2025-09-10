

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
