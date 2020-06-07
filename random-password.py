#!/usr/bin/env python

from random import choice
import datetime
import os

p = ""
valores_caracteres = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
valores_min_may_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
valores_num_min = "0123456789abcdefghijklmnopqrstuvwxyz"
valores_num_may = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
valores_numericos = "0123456789"
valores_min = "abcdefghijklmnopqrstuvwxyz"
valores_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
valores_min_may = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Elige que tipo de caracteres quiere que tenga la password: ")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("1.- Simbolos, Mayusculas, Minusculas y Numeros")
print("2.- Mayusculas, Minusculas y Numeros")
print("3.- Minusculas y Numeros")
print("4.- Mayusculas y Numeros")
print("5.- Solo Numeros")
print("6.- Solo Minusculas")
print("7.- Solo Mayusculas")
print("8.- Minusculas y Mayusculas")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

caracter = input("Ingresa tu seleccion: ")

if caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8":
    if caracter == "1":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_caracteres) for i in range(longitud)])
    elif caracter == "2":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_min_may_num) for i in range(longitud)])
    elif caracter == "3":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_num_min) for i in range(longitud)])
    elif caracter == "4":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_num_may) for i in range(longitud)])
    elif caracter == "5":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_numericos) for i in range(longitud)])
    elif caracter == "6":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_min) for i in range(longitud)])
    elif caracter == "7":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_may) for i in range(longitud)])
    elif caracter == "8":
        longitud = int(input("Longitud de la password: "))
        p = p.join([choice(valores_min_may) for i in range(longitud)])
    else:
        print("Opcion incorrecta")
    print(p)

    if os.path.isdir('passwords'):
        fecha_proceso = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
    
        nombre_archivo = "passwords/" + fecha_proceso + "_password.txt"
        data_out_registros = open(nombre_archivo, "w")
        data_out_registros.write("|||||||||||Tu password es: ||||||||||||\n" + p + "\n" + "|||||||||||||||||||||||||||||||||||||||")
    else:
        print("Se creo el directorio passwords")
        os.mkdir("passwords")
        fecha_proceso = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
    
        nombre_archivo = "passwords/" + fecha_proceso + "_password.txt"
        data_out_registros = open(nombre_archivo, "w")
        data_out_registros.write("|||||||||||Tu password es: ||||||||||||\n" + p + "\n" + "|||||||||||||||||||||||||||||||||||||||")
else:
    print("Ingresa un numero del 1 al 8!!")
