#  Ejercicio 1
# Dados 2 números enteros, imprimir por pantalla el producto.
# Si el producto de ambos numeros es mayor a 100, mostrar además la suma de los numeros.
#
# Se puede utilizar el siguiente código para mostrar por pantalla
# ``` python
# print("El producto entre {} y {} es: {}".format(n1, n2, prod))
# print("La suma entre {} y {} es: {}".format(n1, n2, suma))
# ```
n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))

prod = n1*n2

if prod > 100:
    suma = n1+n2
    print('''
    El producto entre {} y {} es: {}
    La suma entre {} y {}  es: {}'''.format(n1,n2,prod,n1,n2,suma))
else:
    print('El producto entre {} y {} es: {}'.format(n1,n2,prod))

# Ejercicio 2
# Dada una lista de números, se pide iterar los elementos de la lista y almacenar en otra lista el resultado de sumar
# ese elemento con el anterior.
# Por ejemplo, dada la lista: [1, 2, 3, 4], se espera que la salida sea una lista con los elementos [3, 5, 7]
# Resolver el problema de dos maneras diferentes: con un for loop y con una lista por comprensión.
#
# Pistas:
# Iterar la lista, elemento por elemento
# Utilizar variables auxiliares para almacenar información

l_in = [1, 2, 3, 4]
lar = len(l_in)- 1
# esta ultima variable permite que el ciclo for se adapte a cualquier lista, sin importar su extencion.
# el -1 es necesario ya que la lista empieza por el indice 0, si el -1 el resultado seria 4 y daria error en
# el ciclo For
l_b = []

for x in range(0, lar):
    sumaListas = l_in[x+1] + l_in[x]
    l_b.append(sumaListas)

print('''La lista original es: {}
La nueva lista con la suma de los elementos es: {}'''.format(l_in,l_b))

# Ejercicio 3
# Dado un string, mostrar por pantalla unicamente las vocales en formato Mayuscula
# Por ejemplo, el string "Este es un string de prueba" obtendra como output ['E', 'E', 'E', 'U', 'I', 'E', 'U', 'E', 'A']
#
# Resolver el problema de dos maneras diferentes: con un for loop y con una lista por comprensión.
#
# Pistas:
# Utilizar funciones propias de strings como upper, lower

string = 'Nullam suscipit imperdiet libero at euismod'
vocales = ['a','e','i','o','u']
n_s = []

for e in string:
    for v in vocales:
        if e == v:
            nLetra = e.upper()
            n_s.append(nLetra)

print('Las vocales de la string planteada son: {} '.format(n_s))

# Ejercicio 4
# Dada una lista de numeros, mostrar por genere una lista con todos los múltiplos de 7.
# Por ejemplo, para la lista [1, 2, 7, 10, 21], se muestran por pantalla los numeros 7 y 21
#
# Resolver el problema de dos maneras diferentes: con un for loop y con una lista por comprensión.

l_1 = [85, 21, 29, 37, 50, 53, 7, 26, 26, 97, 20, 29, 96, 27, 63, 96, 68,
       60, 47, 18, 3, 34, 63, 48, 16, 43, 91, 29, 92, 45, 5, 98, 36, 23,
       92, 45, 52, 94, 98, 59, 96, 62, 84, 31, 86, 32, 66, 17, 24, 94, 53,
       57, 66, 45, 23, 31, 46, 85, 22, 65, 26, 1, 89, 16, 32, 8, 42, 47,
       38, 92, 41, 25, 98, 49, 24, 23, 12, 59, 6, 56, 35, 44, 19, 64, 7,
       15, 13, 75, 86, 14, 91, 97, 65, 31, 86, 62, 85, 50, 24, 57]

l_2 = []

for n in l_1:
    if n % 7 == 0:
        l_2.append(n)

print('Los multiplos de 7 que estan presente en la lista son: {}'.format(l_2))

# Ejercicio 5
# Contar cuántos elementos de la lista cumple alguna de las siguientes condiciones:
#
# El elemento es un carácter en minúscula y es alfanumérico
# Es un número entero par
# lista = ['a', 2, 5, 'B', 9, 'd', 4, 'o', 7, '%', 3.1, '&']
# Pista:
#
# analizar la función isinstance()

lista_ = ['a', 2, 5, 'B', 9, 'd', 4, 'o', 7, '%', 3.1, '&']
cont_ls = 0

for e in lista_:
    if isinstance(e, str) == True and e.islower() == True:
        cont_ls += 1
    elif isinstance(e, int) == True and e % 2 == 0:
        cont_ls += 1

print('La cantidad de elementos que cumplen con las condiciones son: {}'.format(cont_ls))

# Ejercicio 6
# Obtener el módulo entre el máximo y el mínimo de la siguiente lista.
#
# lista = [893, 755, 708, 746, 801, 581, 187, 688, 492, 579, 469, 195, 918, 667, 7, 15, 212, 114, 635, 331]
# result= 918%7 = 1
#
# Resuelvan el ejercicio de dos formas diferentes: utilizando sin usar las funciones max() y min() y utilizándolas.

lista6 = [893, 755, 708, 746, 801, 581, 187, 688, 492, 579, 469, 195, 918, 667, 7, 15, 212, 114, 635, 331]

mod1 = max(lista6) % min(lista6)

nmax = 0
nmin = 0

for e in lista6:
    if nmin == 0:
        nmin = e
    elif e > nmax:
        nmax = e
    elif e < nmin:
        nmin = e

mod2 = nmax % nmin

print(mod1, mod2)

# Ejercicio 7
# A partir de la siguiente lista de alumnos, obtener el nombre del alumno con mayor nota.

alumnos = {
    "Shelby Snider": 6,
    "Barlow Hammond": 5,
    "Jennifer Simon": 7,
    "Hollie Abbott": 2,
    "Vinson Garcia": 7,
    "Savannah Nunez": 10,
}
nMaxD = 0

for d in alumnos:
    if alumnos[d] > nMaxD:
        nombreA = d

print('El nombre del alumno con mayor nota es: {}'.format(nombreA))
