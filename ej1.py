#!/usr/bin/python3
import os

#Ejercicio 1

#Inicializamos el acumulador
suma = 0

#Primero, definir la lista vacia
vector = []
for i in range(5):
    ingreso = input("Ingresate un numero papurri: ")
    vector.append(int (ingreso))

#Caligula mode
for i in range(5):
    #print(vector[i], end=" ")
    suma = suma + vector[i]

print (suma) # sacalo de aca boludo
os.system('echo "Todos putos"')
