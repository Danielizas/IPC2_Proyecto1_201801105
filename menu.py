import os
from listas import create_circular_linked_list
import xml.etree.ElementTree as ET
clear = lambda: os.system('cls')
lista = create_circular_linked_list()

# C:\Users\danii\Desktop\Proyecto1IPC2\entrada1.xml

def cargar_archivo():
    ruta = input("Ingrese su ruta: ")
    archivo = ET.parse(ruta)
    raiz = archivo.getroot()
    
    for elem in raiz:
        print(elem.get('nombre')," m ",elem.get('m')," n",elem.get('n'))
        for subelem in elem:
            print(subelem.text," x ", subelem.get('x'), "y", subelem.get('y'))
            lista.add_first(elem.get('nombre'))
    lista.travel()

    #for node in raiz.iter():
    #   print(node.tag)




def procesar_archivo():
    print("")

def Datos_estudiante():
    print("Daniel Eduardo Izas Marroquin \n" "201801105\n" 
        "Introduccion a la Programacion y computacion 2 seccion C \n" 
        "Ingenieria en Ciencias y Sistemas\n" 
        "4to Semestre" )

def menu():
    print("Menu principal:")
    print("     1. Cargar Archivo")
    print("     2. Procesar archivo")
    print("     3. Escribir archivo salida")
    print("     4. Mostrar datos del estudiante")
    print("     5. Generar Grafica ")
    print("     6. Salida")
    numero = input("Ingrese una opcion: ")
    return numero

ciclo = True
while(ciclo):
    numero = menu()
    if numero =="1":
        cargar_archivo()
        print("Archivo subido correctamente\n")
    elif numero == "2": 
        print()
    elif numero == "3":
        print()
    elif numero == "4":
        Datos_estudiante()
    elif numero == "5":
        print("")
    elif numero == "6":
        print("salio de la aplicacion")
        ciclo = False