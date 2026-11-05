# print('Hola mundo')
# print('Estoy codeando en python, que pro que soy')
#
# **Variables

# nombre = 'Daniel'
# apellido = 'Jaimes'
# nombre_completo = f'{nombre} {apellido}'
#
# print(f'Hola {nombre_completo}')
# print(type(nombre))

# **metodos para strings

# len() da el tamaño de el string
# find() busca y encuentra en un indice del string
# capiralize() cambia la primera letra del string a mayuscla
# upper() convierta todo el texto en mayus
# lower() convierte todos los caracteres del string en minusculas
# isdigit() confirma si un caracter de una cadena es un digito
# isalpha() confirma si los caracteres son letras
# count() cuenta de acuerdo a un parametro en especifico
# replace() permite reemplazar un argumento con un parametro dado

# nombre = 'daniel'
# print(len(nombre))
# print(nombre.find('i'))
# print(nombre.capitalize())
# print(nombre.upper())
# print(nombre.lower())
# print(nombre.isdigit())
# print(nombre.isalpha())
# print(nombre.count('i'))
# print(nombre.replace('a', 'i'))

# **convertir tipos de datos
# usaremos los metodos
# int() convierte un flotante en integral
# str() convierte en string
# float() convierte en flotante

# **Aceptar entrada de texto

# nombre = input('Cual es tu nombre amig@?')
# edad = int(input('Cual es tu edad amig@?'))
# altura = float(input('Cual es tu altura amig@?'))

# print(f'Hola {nombre}, tu edad es {edad} y mides {altura}')

# **funciones matematicas
# import math

# PI = -3.14
# x = 2
# y = 1
# z = 3

# print(round(PI)) redondea el numero hacia arriba o hacia abajo 
# print(math.ceil(PI)) redondea el numero hacia arriba
# print(math.floor(PI)) redondea el numero hacia abajo
# print(abs(PI)) returna el valor absoluto del numero
# print(math.pow(PI, 2)) potencia(base y exponente)
# print(math.sqrt(420)) raiz cuadrada
# print(max(x, y, z)) returna el numero maximo
# print(min(x, y, z)) retorna el numero minimo

# **manipulacion de cadenas
# para tomar secciones de la cadena
# podremos unsar los signos [] en los
# cuales pondremos los indices de inicio y final
# del corte teniendo en cuenta que el el ultimo
# indice es exclusivo, es decir que no tomara
# la posicion a la que corresponde sino la anterior

# nombre_completo = 'Daniel Jaimes'
# primer_nombre = nombre_completo[: 6]
# apellido = nombre_completo[7:]

# print(primer_nombre)
# print(apellido)

# podemos usar objetos de slice, que cortan de una manera
# mas dinamica los string

# website = 'https://www.google.com'
# slice = slice(12,-4)
# print(website[slice])

# **instrucciones if
# bloque de codigo que se ejecuta solo si la condicion se cumple

#edad = int(input('Digita tu edad: '))

# if edad == 100:
#    print('Eres antiquisimo')
# elif edad >= 18:
#    print('Eres mayor de edad, puedes ingresar')
# else:
#    print('Eres menor de edad, acceso denegado')

# **Operadores logicos
# funcionan para comprobar que si las condiciones son ciertas o falsa
# los operadores mas comunes son and y or

# temperatura = int(input('Cual es la temperatura afuera? '))

# if temperatura >= 0 and temperatura <= 30:
#     print('La temperatura es adecuada hoy ')
# elif temperatura < 0 or temperatura > 30:
#    print('La temperatura no es adecuada ')

# **Bucles while
# es un bucle que se ejecuta mientras la condicion sea cierta

# **Bucles for
# es un bucle que se ejecuta un numero limitado de veces

# **Bucles anidados
# es cuando un bucle se encuentra dentro de otro bucle
# elk bucle interno terminara su proceso antes que el bucle externo

# fila = int(input('Cuantas filas quieres? '))
# columna = int(input('Cuantas columnas quieres? '))
# simbolo = input('Ingrese un simbolo: ')

# for i in range(fila):
#    for j in range(columna):
#        print(simbolo, end='')
#    print()

# **Break Continues Pass
# sentencias para controlar los flujos de los  bucles
# ?Break sirve para detener el el flujo del bucle
# ?Continue salta el flujo normal del bucle
# ?Pass marca la posicion de un flujo, haciendo que se ejecute normalmente

# **Listas en python
# Se usan para guardar multiples elementos en un variable
# en nuestras listas podemos almacenar distintos tipo de datos

# comida = ['pizza', 'hamburguesa', 'hotdog', 'pasta']
# comida[0] = 'lasagna'

# comida.append('pollito') # sirve para agregar un elemento en la parte final de la lista
# comida.remove('hamburguesa') # Remueve un elemento especificado de la lista
# comida.pop()# elimina el ultimo elemento de la lista
# comida.insert(0, 'red velvet')# agrega un elemento en la posiscion especificada
# comida.sort()#organiza la lista alfabeticamente
# comida.clear()#borra todos los elementos de la lista

# for item in comida:
#     print(item)

# **Listas 2D
# listas multidimensionales, son listas que tienen almacenadas otras listas

# bebidas = ['cafe', 'soda', 'te']
# cena = ['pizza', 'hamburguesa', 'hotdog']
# postres = ['pastel','helado']

# comida = [bebidas, cena, postres]

# print(comida)
# print(comida[2][1])

# **Tuplas
# son colecciones ordenadas e inmutables, utiles para agrupar datos relacionados

# estudiantes = ('Dani', 22, 'M', 'Pau', 21, 'f')

# estudiantes.count('Dani') # cuenta cuantas veces aparece un elemento en la tupla
# estudiantes.index('Pau') # devuelve el indice de un elemento en la tupla

# for estudiante in estudiantes:
#     print(estudiante)

# **Sets
# se usan para almacenar elementos al igual de las listas
# no pueden haber elementos duplicados
# No mantienen el orden de cuando son declarados
# Sus elementos son inmutables

# utensilio = {'tenedor', 'cuchara', 'cuchillo'}
# platos = {'plato', 'bowl', 'taza', 'cuchara'}

# utensilio.add('cucharita')
# utensilio.remove('cuchillo')
# utensilio.pop()
# utensilio.clear()
# utensilio.update(platos)
# print(utensilio.difference(platos))

# for i in utensilio:
#    print(utensilio)

# **Diccionario
# es una colleccion modificable y no ordenada de pare unicos clave/valor
# utilizan el concepto de hash
# podemos acceder rapidamente a un valor

# capitales = {
#    'EE.UU': 'Washington D.C',
#    'Argentina': 'Buenos Aires',
#    'Chile': 'Santiago De Chile',
#    'Colombia': 'Bogota D.C'
# }

# print(capitales.get('Argentina'))
# print(capitales.keys())
# print(capitales.values())
# print(capitales.items())

# capitales.update({'Alemania': 'Berlin'})
# capitales.pop('EE.UU')

# for key, value in capitales.items():
#      print(key, value)

# **Operador indice
# nos ayuda a ubicar la posicion de un elemento en un conjunto de datos

# nombre = 'daniel Jaimes'

# if nombre[0].islower():
#     nombre = nombre.capitalize()

# print(nombre)

# primer_nombre = nombre[:6]
# apellido = nombre[7:]

# print(primer_nombre)
# print(apellido)

# **Funciones en Python
# es un bloque de codigo que se ejecuta solo cuando se le llama
# una funcion puede realizar una tarea especifica cuando se le llama

# def saludo(nombre:str):
#    nombre = input('Cual es tu nombre?')
#     print(f'hola {nombre}')
#     print('Que tengas un buen día')

# saludo("Daniel")

# **Return
# nuestras funciones pueden retornar un valor dependiendo de lo que estamos esperando   

# def multiplicar(a,b):
#     return a*b

# x = multiplicar(7,9)
# print(x)

# **Argumentos de palabras clave en python
# son aquellos que se pasan a una función indicando explícitamente el nombre del parámetro mediante la sintaxis

# def saludo(nombre, apellido, lenguaje):
#     print(f'Hola {nombre} {apellido} estas aprendiendo {lenguaje}')

# saludo('Daniel', 'Jaimes', 'Python')
# saludo(lenguaje='C#', nombre='Alejandro', apellido='Jaimes')

# **Funciones anidadas
# son funciones que se llaman desde otra funcion

# print(round(abs(float(input("Ingresa un numero: ")))))

# **Ambito de una variable

# una variable solo esta disponible desde la region que se crea

# def mostrar_nombre():
#     nombre = 'Dani'
#     print(nombre)

# mostrar_nombre()

# **ARG
# es un parametro que empaquetara todos os argumentos en una tupla lo importante es el *, ya que esto es lo que transforma en un tupla el paramatro pasado a la funcion

# def suma(*args):
#    suma = 0
#    for n in args:
#        suma += n
#    return suma

# print(suma(1,5,3,10,2,5,1,2,14,1))

# **Kwargs
# empaqueta todos los argumentos en un diccionario

# def hola(**kwargs):
#     print('Hola', end=' ')
#     for clave, valor in kwargs.items():
#         print(valor, end=' ')

# hola(nombre='Alejandro', apellido='Jimenez')

# **Metodo format
# es un metodo aplicado a las lineas string para dar formato como necesitemos, en los numeros podemos darle formato dependiendo de un sistema de numeracion o mostrar los decimales que necesitamos

# str_1 = 'Leche'
# str_2 = 'casar'

# print(f'Arroz con {str_1} me quiero {str_2}')
# print('Arroz con {} me quiero {}'.format(str_1, str_2))

# texto =  'Arroz con {} me quiero {}'
# print(texto.format(str_1, str_2))

# nombre = 'Daniel'
# print('Hola, Mi nombre es {:10}. Mucho Gusto'.format(nombre))
# print('Hola, Mi nombre es {:<10}. Mucho Gusto'.format(nombre))
# print('Hola, Mi nombre es {:>10}. Mucho Gusto'.format(nombre))
# print('Hola, Mi nombre es {:^10}. Mucho Gusto'.format(nombre))

# numero = 3.141519
# print('El numero PI es {}'.format(numero))
# print('El numero PI es {:.2f}'.format(numero))

# mil = 1000
# print('El numero es {:.2f}'.format(mil))
# print('El numero es {:b}'.format(mil))
# print('El numero es {:o}'.format(mil))
# print('El numero es {:x}'.format(mil))
# print('El numero es {:X}'.format(mil))
# print('El numero es {:e}'.format(mil))

# **Modulo Random
# El metodo random funcionana para generar numeros pseudo aleatorios.

# import random

# x = random.randint(1,6)
# y = random.random()

# piedra_papel_tijera = ['Piedra', 'Papel', 'Tijera']
# z = random.choice(piedra_papel_tijera)

# cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
# random.shuffle(cartas)

# print(x)
# print(y)
# print(z)
# print(cartas)

# **Manejo de excepciones}
# Las excepciones son todos los ventos que interrumpen el flujo de nuestro programa

# try:
# 	numerador = float(input('Ingresa un numero: '))
# 	denominador = float(input('Ingresa un numero: '))
# 	resultado = numerador / denominador
# except ZeroDivisionError as e:
# 	print(e)
# 	print('No puedes dividir por 0')
# except ValueError as e:
# 	print(e)
# 	print('por favor ingresa solo numeros')
# else:
# 	print(resultado)
# finally:
# 	print('esto siempre se va a mostrar')

# **Manejo de archivos
# hoy verificaremos la existencia de archivos, para esto vamos a utilizar el modulo os

# import os

# path = 'F:\\DANI\\Projects\\Python\\assets\\Dani_Documento_Prueba.txt'

# if os.path.exists(path):
#     print('esta ruta existe')
# if os.path.isfile(path):
# 		print('Es un archivo')
# else:
# 	print('esta ruta no existe')

# **Leer un archivo

# path = 'F:\\DANI\\Projects\\Python\\assets\\Dani_Documento_Prueba.txt'

# try:
# 	with open(path) as file:
# 		print(file.read())
# except FileNotFoundError:
# 	print('El archivo no fue encontrado')

# **Escribir un archivo en python

# path = 'F:\\DANI\\Projects\\Python\\assets\\Dani_Documento_Prueba.txt'
# texto ='Hola\nEsto es un poco de texto\nQue tengas un buen dia'

# with open(path, 'w') as file:
# 	file.write(texto)

# with open(path, 'r') as file:
#	print(file.read())

# **Copiando archivos

# import shutil

# shutil.copyfile('F:\\DANI\\Projects\\Python\\assets\\Dani_Documento_Prueba.txt', 'F:\\DANI\\Projects\\Python\\assets\\copy.txt')

# **Moviendo archivos

# import os

# origen = 'testMovimentFile.txt'
# destino = 'F:\\DANI\\Projects\\Python\\assets\\testMovimentFile.txt'

# try:
# 	if os.path.exists(destino):
# 		print(f'ya existe un archivo en {destino}')
# 	else:
# 		os.replace(origen, destino)
# 		print(f'{origen} -> {destino}')
# except FileNotFoundError:
# 	print(f'{origen} File not found')

# **Eliminar archivos

# import os
# import shutil

# path = 'F:\\DANI\\Projects\\Python\\assets\\FolderDeleteTest'

# try:
	# os.remove(path)
	# os.rmdir(path)
	# shutil.rmtree(path)
# except FileNotFoundError:
# 	print("File not exist")
# except PermissionError:
# 	print("Permission denied")
# except OSError:
# 	print('the Folder is not empty')
# else:
# 	print(f"{path} deleted")

# **Modulos
# Es un archivo que contiene codigo que puedes utilizar llamandolo desde tu archivo

# import Modulo as mensaje
# from Modulo import hola, despedida

# hola()
# despedida()

help('modules')