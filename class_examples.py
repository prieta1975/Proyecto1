#Asignación múltiple
a, b = 'Alice', 'Bob'
b, a = a, b
print (a)
print (b)

#Operadores aritméticos
#Suma
n = 2 + 3 + 6
print (n)
#Orden de operaciones
n = (2 + 3) * 6
print (n)
#Producto
n = 48565878 * 578453
print (n)
#Potencias
n = 2 ** 8
print (n)
#División
n = 23 / 7
print (n)
#División entera
n = 23 // 7
print (n)
#Módulo
n = 23 % 7
print (n)
#Incrementar
n += 2
print (n)
#Decrementar
n -= 1
print (n)
""" Esto es un comentario ...
...
multilinea..."""

""" Tipos de datos """
#Entero
num = 20
print(type(num))
#Cadena de caracteres
cadena = "Hola"
print(type(cadena))
#Float
num = 1.234
print(type(num))
#Imaginarios
num = 3+5J
print(type(num))

""" Cadenas de Texto. Las cadenas de texto son inmutables, esto es, no se les pueden hacer asignaciones por índices """
palabra = 'Python'
print(palabra[0])   #Imprime el primer carácter, comienzo desde 0
print(palabra[5])   #Imprime el sexto carácter, comienzo desde 0
print(palabra[-1])  #Imprime el último carácter, indexado desde el final, comienzo -1
print(palabra[-6])  #Imprime el primer carácter, indexado desde el final, comienzo -1
print(palabra[0:2]) #Imprime los caracteres desde el 0 (incluido) hasta el 2 (excluido)
print(palabra[0:5]) #Imprime los caracteres desde el 0 (incluido) hasta el 5 (excluido)
print(palabra[0:6]) #Imprime los caracteres desde el 0 (incluido) hasta el 6 (excluido)

print(palabra[:2] + palabra[2:])    #Nota: el primero es siempre incluído, y  el último es siempre excluído. Esto asegura que s[:i] + s[i:] siempre sea igual a s: 

palabra2 = 'J' + palabra[1:]
print(palabra2)
print(len(palabra2))

""" LISTAS """
cuadrados = [1, 4, 9, 16, 25]
print(cuadrados)
print(cuadrados[0])
print(cuadrados[0:3])
print(cuadrados[-3:])

cuadrados += [36, 49, 64, 81, 100]  # Añade elementos a la lista
print(cuadrados)

cuadrados[0] = 0    #Se pueden cambiar elementos de la lista por índice
print(cuadrados)

cuadrados.append(121)   #Adición de un elemento a la lista
print(cuadrados)

print(len(cuadrados))   #Imprime la longitus de elementos en la cadena

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
letras[2:5] = ['C', 'D', 'E']   #Reemplaza las posiciones 2 a 4 por nuevos valores
print(letras)
letras[2:5]=[]                  #Elimina las posiciones 2 a 5
print(letras)
letras[:]=[]                    #Elimina todas las posiciones de la lista
print(letras)

#Se pueden anidar listas en listas
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])

''' Tuplas: Tuple is similar to a list except you cannot change elements of a tuple once it is defined. Whereas in a list, items can be modified.
    Basically, list is mutable whereas tuple is immutable. '''

language = ("French", "German", "English", "Polish")
print(language)
print(language[0])
print(language[-1])
del language

''' Sets: A set is an unordered collection of items where every element is unique (no duplicates).'''

my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set of integers
my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.add(2)
print(my_set) # Output: {1, 2, 3, 4}

my_set.update([3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set) # Output: {1, 2, 3, 5}


A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B) 
# Also equivalent to B.union(A)
print(A | B) # Output: {1, 2, 3, 4, 5}

# Equivalent to A.intersection(B)
# Also equivalent to B.intersection(A)
print (A & B) # Output: {2, 3}

# Set Difference
print (A - B) # Output: {1}

# Set Symmetric Difference
print(A ^ B)  # Output: {1, 4, 5}

'''Diccionarios: Dictionary is an unordered collection of items. 
    While other compound data types have only value as an element, a dictionary has a key: value pair. For example:'''

    # empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

person = {'name':'Jack', 'age': 26, 'salary': 4534.2}
print(person['age']) # Output: 26

''' Here's how you can change, add or delete dictionary elements.'''

person = {'name':'Jack', 'age': 26}

# Changing age to 36
person['age'] = 36 
print(person) # Output: {'name': 'Jack', 'age': 36}

# Adding salary key, value pair
person['salary'] = 4342.4
print(person) # Output: {'name': 'Jack', 'age': 36, 'salary': 4342.4}


# Deleting age
del person['age']
print(person) # Output: {'name': 'Jack', 'salary': 4342.4}

# Deleting entire dictionary
del person

''' Rangos '''

print(range(1,10))

numbers = range(1, 6)

print(list(numbers)) # Output: [1, 2, 3, 4, 5]
print(tuple(numbers)) # Output: (1, 2, 3, 4, 5)
print(set(numbers)) # Output: {1, 2, 3, 4, 5}

# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99} 
print(dict.fromkeys(numbers, 99))


#Equivalent to: numbers = range(1, 6)
numbers1 = range(1, 6 , 1)
print(list(numbers1)) # Output: [1, 2, 3, 4, 5]

numbers2 = range(1, 6, 2)
print(list(numbers2)) # Output: [1, 3, 5]

numbers3 = range(5, 0, -1)
print(list(numbers3)) # Output: [5, 4, 3, 2, 1]


''' if...else '''

num = -1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
# Output: Negative number

'''There can be zero or more elif parts, and the else part is optional.

Most programming languages use {} to specify the block of code. Python uses indentation.

A code block starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.

Generally, four whitespace is used for indentation and is preferred over tabs.'''

if False:
    print("I am inside the body of if.")
    print("I am also inside the body of if.")
print("I am outside the body of if")

# Output: I am outside the body of if.

''' while loop '''

n = 100

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

# Output: The sum is 5050

''' for Loop '''

numbers = [6, 5, 3, 8, 4, 2]

sum = 0

# iterate over the list
for val in numbers:
  sum = sum+val

print("The sum is", sum) # Output: The sum is 28



for val in "string":
    if val == "r":
        break
    print(val)

print("The end")



for val in "string":
    if val == "r":
        continue
    print(val)

print("The end")


sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass


''' Funciones '''

def print_lines():
  print("I am line1.")
  print("I am line2.")

# function call
print_lines()



def add_numbers(a, b):
  sum = a + b
  print(sum)

add_numbers(4, 5)

# Output: 9



def add_numbers2(a, b):
  sum = a + b
  return sum

result = add_numbers2(4, 5)
print(result)

# Output: 9



# Recursive function to find the factorial of a number

def calc_factorial(x):

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 6
print("The factorial of", num, "is", calc_factorial(num)) 

# Output: The factorial of 6 is 720



''' Lambda Function

In Python, you can define functions without a name. These functions are called lambda or anonymous function. 
To create a lambda function, lambda keyword is used.'''

square = lambda x: x ** 2
print(square(5))

# Output: 25


''' Python File I/O '''

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()


import os

print(os.getcwd())  # present working directory
#os.chdir('D:\\Hello') # Changing current directory to D:\Hello
#os.listdir()  # list all sub directories and files in that path
#os.mkdir('test') # making a new directory test
#os.rename('test','tasty') # renaming the directory test to tasty
#os.remove('old.txt')  # deleting old.txt file

