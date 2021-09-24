# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:08:21 2017

@author: Vuctor
"""
Día = int(input("ingrese su día de nacimiento: "))
Mes = input("ingresa su mes de nacimiento: ")
Año = int(input("ingrese su año de nacimiento: "))
r= int((2017 - Año)*365 + ((2017 - Año)/4))
if Mes == "enero" or (Mes == "febrero" and Día <= 18):
    print("Su signo del zodiaco es: Acuario")
if (Mes == "febrero" and Día>= 19) or (Mes == "marzo" and Día <= 20):
    print("Su signo del zodiaco es: Piscis")
if (Mes == "marzo" and Día >= 21) or (Mes == "abril" and Día <= 19):
    print("Su signo del zodiaco es: Aries")
if (Mes == "abril" and Día >= 20 ) or (Mes == "mayo" and Día <= 20):
    print("Su signo del zodiaco es: Tauro")
if (Mes == "mayo" and Día >= 21 ) or (Mes == "junio" and Día <= 20):
    print("Su signo del zodiaco es: Gémenis")
if (Mes == "junio" and Día >= 21 ) or (Mes == "julio" and Día <= 22):
    print("Su signo del zodiaco es: Cáncer")
if (Mes == "julio" and Día >= 23 ) or (Mes == "agosto" and Día <= 22):
    print("Su signo del zodiaco es: Leo")    
if (Mes == "agosto" and Día >= 23 ) or (Mes == "septiembre" and Día <= 22):
    print("Su signo del zodiaco es: Virgo")
if (Mes == "septiembre" and Día >= 23 ) or (Mes == "octubre" and Día <= 22):
    print("Su signo del zodiaco es: Libra")
if (Mes == "octubre" and Día >= 23 ) or (Mes == "noviembre" and Día <= 21):
    print("Su signo del zodiaco es: Escorpión")
if (Mes == "noviembre" and Día >= 22 ) or (Mes == "diciembre" and Día <= 21):
    print("Su signo del zodiaco es: Sagitario")
if (Mes == "diciembre" and Día >= 22 ) or (Mes == "enero" and Día <= 19):
    print("Su signo del zodiaco es: Capricornio")  
print("Y su edad en días es: ", r)