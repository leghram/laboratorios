colores = ['rojo', 'azul', 'verde', 'amarillo']

print(colores)


#posicion en las listas
colores = ['rojo', 'azul', 'verde', 'amarillo']

print(colores[0])




varios = ['rojo', 7, 10]
 
suma = varios[1] + varios[2]
 
print(f'Mi color favorito es el {varios[0]} y la suma de {varios[1]} y {varios[2]}, da como resultado: {suma}.')





#ultimo valor de la lista
colores = ['rojo', 'azul', 'verde', 'amarillo']
 
print(colores[-1])



#agregando valores a la lsita
colores = ['rojo', 'azul', 'verde', 'amarillo']
 
colores.append('gris')
 
print(colores)



#insertando valores en posiciones especificas

colores = ['rojo', 'azul', 'verde', 'amarillo']
 
colores.insert(2,'gris')
 
print(colores)




#eliminando valores de la lista 

colores = ['rojo', 'azul', 'verde', 'amarillo']
 
colores.pop(0)
print(colores)



#ordenando los datos de la lista

colores = ['rojo', 'azul', 'verde', 'amarillo']
 
colores.sort()
print(colores)


colores = ['rojo', 'azul', 'verde', 'amarillo']
 
colores.sort(reverse=True)
print(colores)