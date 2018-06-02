#!/usr/bin/python3

vector = []
max = False
pos = 0

#Cargamos el vector
for i in range(50):
    vector.append(i)

for i in vector:
    if max == False:
        max = vector[i]
#    else:
        if vector[i] > max:
            max = vector[i]

print(max)
