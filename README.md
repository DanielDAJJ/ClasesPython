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

## Conclusión

Este archivo funciona como una guía introductoria a Python, cubriendo desde conceptos básicos como variables y salida por consola, hasta estructura de datos, ciclos, condiciones y funciones. Es una base ideal para comenzar a programar con Python.
