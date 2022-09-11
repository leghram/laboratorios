# Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo
cadena = "Hola\nMundo"  

# Saldrá una única línea en pantalla y la \ y la n será visibles como caracteres normales.
cadena2 = r"Hola\nMundo"

cadena = "Hola Mundo"
for letra in cadena:
   print(letra)


cadena = "Hola Mundo"

# Saca por pantalla la 'a' de 'Hola Mundo'
print (cadena[3])

# Saca por pantalla el último carácter, la 'o'
print (cadena[-1])


cadena = "Hola Mundo"

# Saca por pantalla 'ol'
print (cadena[1:3])

#Saca por pantalla 'Hol'
print (cadena[:3])

# Saca por pantalla ' Mundo' (con el espacio delante)
print (cadena[4:])

# Saca por pantalla 'un'
print (cadena[-4:-2])

# Saca por pantalla 'undo'
print (cadena[-4:])

# Saca por pantalla 'Hola Mun'
print (cadena[:-2])



cadena = "Hola Mundo"

print(cadena.find("Hola"))        # Devuelve posición 0
print(cadena.find("Mundo"))       # Devuelve posición 5

print(cadena.find("Hola", 3))     # Devuelve -1, a partir de la posición 3 de "Hola Mundo" no hay ningún "Hola"
print(cadena.find("Mundo", 3))    # Devuelve 5, a partir de la posición 3 de "Hola Mundo" hay un "Mundo".

print(cadena.find("Hola", 0, 5))  # Devuelve 0, hay un "Hola" entre la posición 0 y 5 de "Hola Mundo".
print(cadena.find("Mundo", 0, 5)) # Devuelve -1, no hay un "Mundo" entre la posición 0 y 5 de "Hola Mundo".




# print ( "string formato" % valores)
# Un ejemplo concreto

# Esto saca en pantalla "El valor es 11"
print ("El valor es %d" % 11)

# Si hay varios valores, van entre paréntesis
# Esto saca en pantalla "Los valores son 11 y 33"
print ("Los valores son %d y %d" % (11,33))




# saca "El valor es 12
print ("El valor es {}".format(12))

# saca "El valor es 12.3456
print ("El valor es {}".format(12.3456))

# Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
# y así sucesivamente.
# saca "Los valores son 1, 2 y 3"
print ("Los valores son {}, {} y {}".format(1,2,3))

# Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
# {0} es el primer parámetro de format.
# saca "Los valores son 3, 2 y 1"
print ("Los valores son {2}, {1} y {0}".format(1,2,3))





# Los textos para la cabecera de la tabla
cabecera = ('texto izquierda','texto derecha','texto centrado','numero')

# Los valores. Declaramos y vamos rellenando con un bucle
valores = []

for valor in range(10):
    valores.append((f'texto {valor}',f'texto {valor}',f'texto {valor}', 53/(valor+1)))

# Sacamos la cabecera, 20 caracteres cada columna mas un | de separación
print (f'{cabecera[0]:<20} |',f'{cabecera[1]:>20} |',f'{cabecera[2]:^20} |',f'{cabecera[3]:>20}')

# Sacamos los valores, 20 caracteres cada columna mas un | de separación
for valor in valores:
    print (f'{valor[0]:<20} |',f'{valor[1]:>20} |',f'{valor[2]:^20} |',f'{valor[3]:20.4f}')


