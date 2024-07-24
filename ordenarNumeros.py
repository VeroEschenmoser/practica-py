'''Cree un programa que reciba 2 números como entrada y los ordene de menor a mayor. '''

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

if numero1 > numero2:
    print(f'{numero2}, {numero1}')
else:
    print(f'{numero1}, {numero2}')

# Luego modificar el programa para que permita ingresar 3 números. 

""" numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))

if numero1 > numero2:
    if numero1 > numero3:
        if numero2 > numero3:
            print(f'{numero3}, {numero2}, {numero1}')
        else:
            print(f'{numero2}, {numero3}, {numero1}')
    else:
        print(f'{numero2}, {numero1}, {numero3}')
else:
    if numero2 > numero3:
        if numero1 > numero3:
            print(f'{numero3}, {numero1}, {numero2}')
        else:
            print(f'{numero1}, {numero3}, {numero2}')
    else:
        print(f'{numero1}, {numero2}, {numero3}') """


# Por último volver a modificarlo para que permita ingresar “n” números y devolverlos ordenados.

""" lista_numeros = []

while True:
    numero = input("Ingrese un número o 'fin' para terminar: ")
    if numero == 'fin':
        break
    lista_numeros.append(int(numero))
 """
# op1 (sort)
""" lista_numeros.sort() """

# op2 (ordenamiento burbuja)
# se puede aprovechar y explicar el algoritmo de ordenamiento burbuja
""" for numPasada in range(len(lista_numeros)-1,0,-1):
    for i in range(numPasada):
        print(i)
        if lista_numeros[i]>lista_numeros[i+1]:
            temp = lista_numeros[i]
            lista_numeros[i] = lista_numeros[i+1]
            lista_numeros[i+1] = temp
 """

""" print(lista_numeros) """

#Encuentras alguna manera de hacerlo más eficiente?