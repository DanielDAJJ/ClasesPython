# Python Fundamentals

Este proyecto reúne conceptos básicos de Python aprendidos en `main.py`, con ejemplos prácticos para comprender el uso de variables, cadenas, estructuras de datos, condiciones, ciclos y funciones.

## 1. Hola mundo

```python
print('Hola mundo')
```

Es la forma más simple de mostrar un mensaje en la consola.

## 2. Variables

Las variables permiten guardar información para usarla después.

```python
nombre = 'Daniel'
apellido = 'Jaimes'
nombre_completo = f'{nombre} {apellido}'

print(f'Hola {nombre_completo}')
print(type(nombre))
```

En Python puedes guardar texto, números y otros tipos de datos en variables.

## 3. Métodos para strings

Los strings tienen varios métodos útiles:

- `len()`: devuelve la longitud del texto
- `find()`: busca una cadena dentro de otra
- `capitalize()`: pone la primera letra en mayúscula
- `upper()`: convierte a mayúsculas
- `lower()`: convierte a minúsculas
- `isdigit()`: verifica si es un número
- `isalpha()`: verifica si son solo letras
- `count()`: cuenta coincidencias
- `replace()`: reemplaza texto por otro

```python
nombre = 'daniel'
print(len(nombre))
print(nombre.find('i'))
print(nombre.capitalize())
print(nombre.upper())
print(nombre.lower())
print(nombre.isdigit())
print(nombre.isalpha())
print(nombre.count('i'))
print(nombre.replace('a', 'i'))
```

## 4. Conversión de tipos

Python permite convertir datos entre tipos:

- `int()`: convierte a entero
- `str()`: convierte a texto
- `float()`: convierte a decimal

```python
numero = float('3.14')
print(int(numero))
print(str(numero))
```

## 5. Entrada de datos

La función `input()` permite recibir información desde el usuario.

```python
nombre = input('Cual es tu nombre amig@?')
edad = int(input('Cual es tu edad amig@?'))
altura = float(input('Cual es tu altura amig@?'))

print(f'Hola {nombre}, tu edad es {edad} y mides {altura}')
```

## 6. Funciones matemáticas

Python puede trabajar con operaciones matemáticas usando el módulo `math`.

```python
import math

PI = -3.14
x = 2
y = 1
z = 3

print(round(PI))
print(math.ceil(PI))
print(math.floor(PI))
print(abs(PI))
print(math.pow(PI, 2))
print(math.sqrt(420))
print(max(x, y, z))
print(min(x, y, z))
```

Algunas funciones útiles:

- `round()`: redondea
- `ceil()`: redondea hacia arriba
- `floor()`: redondea hacia abajo
- `abs()`: valor absoluto
- `pow()`: potencia
- `sqrt()`: raíz cuadrada
- `max()` y `min()`: máximo y mínimo

## 7. Manipulación de cadenas

Se pueden extraer porciones de texto con slicing.

```python
nombre_completo = 'Daniel Jaimes'
primer_nombre = nombre_completo[:6]
apellido = nombre_completo[7:]

print(primer_nombre)
print(apellido)
```

También se puede usar `slice()` para cortar cadenas de manera más dinámica:

```python
website = 'https://www.google.com'
slice = slice(12, -4)
print(website[slice])
```

## 8. Condicionales `if`

Las instrucciones `if` permiten ejecutar bloques de código solo cuando se cumple una condición.

```python
edad = int(input('Digita tu edad: '))

if edad == 100:
    print('Eres antiquisimo')
elif edad >= 18:
    print('Eres mayor de edad, puedes ingresar')
else:
    print('Eres menor de edad, acceso denegado')
```

## 9. Operadores lógicos

Los operadores lógicos sirven para comparar varias condiciones:

- `and`: ambas condiciones deben cumplirse
- `or`: al menos una debe cumplirse

```python
temperatura = int(input('Cual es la temperatura afuera? '))

if temperatura >= 0 and temperatura <= 30:
    print('La temperatura es adecuada hoy')
elif temperatura < 0 or temperatura > 30:
    print('La temperatura no es adecuada')
```

## 10. Bucles `while` y `for`

### `while`

Un ciclo `while` se ejecuta mientras la condición siga siendo verdadera.

### `for`

Un ciclo `for` se ejecuta un número determinado de veces.

### Bucles anidados

Cuando un ciclo se encuentra dentro de otro, el interior se ejecuta antes que el exterior.

```python
fila = int(input('Cuantas filas quieres? '))
columna = int(input('Cuantas columnas quieres? '))
simbolo = input('Ingrese un simbolo: ')

for i in range(fila):
    for j in range(columna):
        print(simbolo, end='')
    print()
```

## 11. `break`, `continue` y `pass`

Estos comandos controlan el flujo de los bucles:

- `break`: corta el ciclo
- `continue`: salta a la siguiente iteración
- `pass`: deja el lugar vacío y continúa normalmente

## 12. Listas

Las listas permiten almacenar varios elementos en una sola variable.

```python
comida = ['pizza', 'hamburguesa', 'hotdog', 'pasta']
comida[0] = 'lasagna'

comida.append('pollito')
comida.remove('hamburguesa')
comida.pop()
comida.insert(0, 'red velvet')
comida.sort()
comida.clear()

for item in comida:
    print(item)
```

Métodos útiles:

- `append()`: agrega un elemento al final
- `remove()`: elimina un elemento específico
- `pop()`: elimina el último elemento
- `insert()`: inserta en una posición
- `sort()`: ordena la lista
- `clear()`: elimina todo

## 13. Listas 2D

Las listas multidimensionales contienen otras listas dentro de ellas.

```python
bebidas = ['cafe', 'soda', 'te']
cena = ['pizza', 'hamburguesa', 'hotdog']
postres = ['pastel', 'helado']

comida = [bebidas, cena, postres]

print(comida)
print(comida[2][1])
```

## 14. Tuplas

Las tuplas son colecciones ordenadas e inmutables.

```python
estudiantes = ('Dani', 22, 'M', 'Pau', 21, 'f')

print(estudiantes.count('Dani'))
print(estudiantes.index('Pau'))

for estudiante in estudiantes:
    print(estudiante)
```

Son útiles cuando se desea guardar datos que no deben cambiar.

## 15. Sets

Los sets almacenan elementos sin duplicados y sin mantener necesariamente un orden.

```python
utensilio = {'tenedor', 'cuchara', 'cuchillo'}
platos = {'plato', 'bowl', 'taza', 'cuchara'}

utensilio.add('cucharita')
utensilio.remove('cuchillo')
utensilio.pop()
utensilio.clear()
utensilio.update(platos)
print(utensilio.difference(platos))
```

## 16. Diccionarios

Los diccionarios guardan pares clave-valor.

```python
capitales = {
    'EE.UU': 'Washington D.C',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago De Chile',
    'Colombia': 'Bogota D.C'
}

print(capitales.get('Argentina'))
print(capitales.keys())
print(capitales.values())
print(capitales.items())

capitales.update({'Alemania': 'Berlin'})
capitales.pop('EE.UU')

for key, value in capitales.items():
    print(key, value)
```

## 17. Operador de índice

Permite acceder a posiciones específicas dentro de una cadena o estructura.

```python
nombre = 'daniel Jaimes'

if nombre[0].islower():
    nombre = nombre.capitalize()

print(nombre)

primer_nombre = nombre[:6]
apellido = nombre[7:]

print(primer_nombre)
print(apellido)
```

## 18. Funciones en Python

Una función es un bloque de código reutilizable.

```python
def saludo(nombre: str):
    print(f'hola {nombre}')
    print('Que tengas un buen día')

saludo('Daniel')
```

## 19. `return`

Las funciones pueden devolver un valor usando `return`.

```python
def multiplicar(a, b):
    return a * b

resultado = multiplicar(5, 4)
print(resultado)
```

## 20. Argumentos con nombre

Los argumentos con nombre (keyword arguments) se pasan indicando el nombre del parámetro. Así, el orden de los argumentos puede variar.

```python
def saludo(nombre, apellido, lenguaje):
    print(f'Hola {nombre} {apellido} estas aprendiendo {lenguaje}')

saludo('Daniel', 'Jaimes', 'Python')
saludo(lenguaje='C#', nombre='Alejandro', apellido='Jaimes')
```

## 21. Funciones anidadas y ámbito de variables

Una función anidada se llama desde otra función. El ámbito determina desde qué partes del programa se puede acceder a una variable. Una variable creada dentro de una función es local a esa función.

```python
def mostrar_nombre():
    nombre = 'Dani'
    print(nombre)

mostrar_nombre()
```

Las funciones también se pueden combinar para transformar una entrada en varios pasos:

```python
print(round(abs(float(input('Ingresa un numero: ')))))
```

## 22. `*args` y `**kwargs`

`*args` agrupa argumentos posicionales adicionales en una tupla. `**kwargs` agrupa argumentos con nombre adicionales en un diccionario.

```python
def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(suma(1, 5, 3, 10))
```

```python
def hola(**kwargs):
    print('Hola', end=' ')
    for valor in kwargs.values():
        print(valor, end=' ')

hola(nombre='Alejandro', apellido='Jimenez')
```

## 23. Formato de strings

El método `format()` permite insertar valores en un string y controlar cómo se muestran, por ejemplo, su alineación, cantidad de decimales o representación numérica.

```python
nombre = 'Daniel'
numero = 3.141519

print('Hola, mi nombre es {:10}. Mucho gusto'.format(nombre))
print('El numero PI es {:.2f}'.format(numero))
print('El numero es {:b}'.format(1000))  # binario
```

También se pueden usar f-strings para insertar valores:

```python
str_1 = 'Leche'
str_2 = 'casar'
print(f'Arroz con {str_1} me quiero {str_2}')
```

## 24. Módulo `random`

El módulo `random` genera valores pseudoaleatorios y permite elegir o mezclar elementos de una colección.

```python
import random

print(random.randint(1, 6))  # entero entre 1 y 6, inclusive
print(random.random())       # decimal entre 0 y 1
print(random.choice(['Piedra', 'Papel', 'Tijera']))

cartas = ['1', '2', '3', 'J', 'Q', 'K', 'A']
random.shuffle(cartas)
print(cartas)
```

## 25. Manejo de excepciones

Las excepciones son errores que pueden interrumpir el flujo del programa. `try` y `except` permiten manejarlos; `else` se ejecuta si no hubo error y `finally` se ejecuta siempre.

```python
try:
    numerador = float(input('Ingresa un numero: '))
    denominador = float(input('Ingresa otro numero: '))
    resultado = numerador / denominador
except ZeroDivisionError:
    print('No puedes dividir por 0')
except ValueError:
    print('Por favor ingresa solo numeros')
else:
    print(resultado)
finally:
    print('Esto siempre se va a mostrar')
```

## 26. Manejo de archivos y carpetas

El módulo `os` permite comprobar si una ruta existe y si corresponde a un archivo. Usa rutas relativas para que los ejemplos funcionen en distintos equipos.

```python
import os

path = 'assets/ejemplo.txt'

if os.path.exists(path):
    print('La ruta existe')
    if os.path.isfile(path):
        print('Es un archivo')
else:
    print('La ruta no existe')
```

### Leer y escribir archivos

`with open(...)` administra la apertura y el cierre del archivo. El modo `'r'` lee y el modo `'w'` escribe, reemplazando el contenido existente.

```python
path = 'assets/ejemplo.txt'

try:
    with open(path, 'r', encoding='utf-8') as archivo:
        print(archivo.read())
except FileNotFoundError:
    print('El archivo no fue encontrado')
```

```python
texto = 'Hola\nEsto es un poco de texto\nQue tengas un buen dia'

with open(path, 'w', encoding='utf-8') as archivo:
    archivo.write(texto)
```

### Copiar, mover y eliminar

El módulo `shutil` copia archivos y carpetas; `os.replace()` puede mover un archivo. `os.remove()` elimina archivos, `os.rmdir()` elimina carpetas vacías y `shutil.rmtree()` elimina carpetas y su contenido.

```python
import os
import shutil

shutil.copyfile('assets/ejemplo.txt', 'assets/copia.txt')

origen = 'ejemplo.txt'
destino = 'assets/ejemplo.txt'
if os.path.exists(destino):
    print(f'Ya existe un archivo en {destino}')
else:
    os.replace(origen, destino)
```

Ten cuidado al usar operaciones de eliminación, especialmente `shutil.rmtree()`, porque borra recursivamente el contenido de una carpeta.

## 27. Módulos propios

Un módulo es un archivo Python que contiene código reutilizable. Se puede importar el módulo completo con un alias o importar funciones específicas.

```python
import Modulo as mensaje
from Modulo import hola, despedida

hola()
despedida()
```

La instrucción `help('modules')` muestra los módulos disponibles en la instalación de Python.

## Conclusión

Este archivo funciona como una guía introductoria a Python, desde variables, strings y estructuras de datos hasta funciones, excepciones, archivos y módulos. Los ejemplos de `main.py` están comentados y sirven como referencia para practicar cada concepto.
