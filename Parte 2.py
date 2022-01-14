# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion del menú: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

def Crear_vector():  
    
    for i in range (1000):
        vector.append(np.random.randint(1, 1000))            
                  
    print (vector)

def Mayor_menor_burbuja(vector):
    for i in range(1,len(vector)):
        for j in range(0,len(vector)-i):
            if(vector[j+1] > vector[j]):
                aux=vector[j];
                vector[j]=vector[j+1];
                vector[j+1]=aux;
          
def Menor_mayor_burbuja(vector):
    for i in range(1,len(vector)):
        for j in range(0,len(vector)-i):
            if(vector[j+1] < vector[j]):
                aux=vector[j];
                vector[j]=vector[j+1];
                vector[j+1]=aux;


vector = [ ]
salir = False
opcion = 0
 
while not salir:
 
    print ("")    
    print ("1. Llenar vector con 1000 elementos aleatorios e imprimirlo")
    print ("2. Crear archivo Numeros.txt")
    print ("3. Ordenar de mayor a menor")
    print ("4. Crear archivo aleatorios_ordenados.txt")
    print ("5. Ordenar menor a mayor")
    print ("6. Crear archivo final_invertidos.txt")
    print ("7. Salir")
     
    print ("Elige una opcion")
 
    opcion = Menu()
 
    if opcion == 1:
        Crear_vector()        
    elif opcion == 2:        
        np.savetxt('Numeros.txt', vector, fmt='%d')        
    elif opcion == 3:
       Mayor_menor_burbuja(vector);
       print (vector)
    elif opcion == 4:
        np.savetxt('Aleatorios_ordenados.txt', vector, fmt='%d')
    elif opcion == 5:
        Menor_mayor_burbuja(vector);
        print (vector)
    elif opcion == 6:
        np.savetxt('Final_invertidos.txt', vector, fmt='%d')
    elif opcion == 7:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 7")
 
print ("Fin")









