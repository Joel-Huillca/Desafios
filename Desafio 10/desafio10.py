# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 21:55:12 2017

@author: joelh
"""

import numpy as np

fechas = []
actividades = []
minutos = np.zeros([15,15])
sumaActividades= []
mayores= []
menores= []

mayor=-9999999
menor=9999999

arch = open("gaby.txt","r")

nombre = arch.readline().strip().split(" ")
while nombre[0] != "" :
    
    if not nombre[0] in fechas:
        fechas.append(nombre[0])
        sumaActividades.append(0)
        
    if not nombre[1] in actividades:
        actividades.append(nombre[1])
    
    nombre = arch.readline().strip().split(" ")

fechas.sort()

arch = open("gaby.txt","r")

nombre = arch.readline().strip().split(" ")
while nombre[0] != "" :
    posF = fechas.index(nombre[0])
    posA = actividades.index(nombre[1])
    minutos[posF][posA] += int(nombre[2])
    sumaActividades[posF] += int(nombre[2])

    nombre = arch.readline().strip().split(" ")

for i in range(len(fechas)):
    for a in range(len(actividades)):
        if minutos[i][a] > 0:
            if int(minutos[i][a]) > mayor:
                mayor = minutos[i][a]
            if int(minutos[i][a]) < menor:
                menor = minutos[i][a]
    for b in range(len(actividades)):
        if int(minutos[i][b]) == mayor:
            mayores.append(0)
            if mayores[i] == 0:
                mayores[i] = (int(minutos[i][b]))
        if int(minutos[i][b]) == menor:
            menores.append(0)
            if menores[i] == 0:
                menores[i] = (int(minutos[i][b]))

    mayor=-999999
    menor=999999
            
for i in range(len(fechas)):
    print(" ")
    print(fechas[i])
    print("Mayor tiempo:")
    for a in range(len(fechas)):
            if int(minutos[i][a]) == mayores[i]:
                print(actividades[a]+"("+str(mayores[i])+")")
    print("Menor tiempo:")
    for b in range(len(fechas)):
        if int(minutos[i][b]) == menores[i]:
            print(actividades[b]+"("+str(menores[i])+")")
    porcentaje = (int(sumaActividades[i]) * 100) / 960
    print("Total Minutos: "+str(sumaActividades[i])+" ("+str(round(porcentaje,2))+"%)")
    
    
    
    
    