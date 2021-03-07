import os
from listas import create_circular_linked_list
import xml.etree.ElementTree as ET
clear = lambda: os.system('cls')
lista = create_circular_linked_list()

# C:\Users\danii\Desktop\Proyecto1IPC2\entrada1.xml
# C:\Users\danii\Desktop\Proyecto1IPC2\Archivoprueba.xml
def cargar_archivo():
    ruta = input("Ingrese su ruta: ")
    archivo = ET.parse(ruta)
    raiz = archivo.getroot()
    
    datname = []
    child = []
    l =0
    for elem in raiz:
        name = str(elem.get('nombre'))
        mcol = str(elem.get('m'))
        nfil = str(elem.get('n'))
        #print(elem.get('nombre')," n ",elem.get('n')," m",elem.get('m'))
        for subelem in elem:
            x = str(subelem.get('x'))
            y = str(subelem.get('y'))
            res = str(subelem.text)
            datname = [x, y, res]
            child.append(datname)
            #print(subelem.text," x ", subelem.get('x'), "y", subelem.get('y'))
        if l ==0:
            lista.add_first(name, nfil, mcol, child)
        else:
            lista.add_last(name, nfil, mcol, child)
        datname = []
        child = []    
        l= l+1

    lista.travel('nombre','n','m','datos')



def procesar_archivo():
    matriz = input("Ingrese la matriz indicada")
    lista.is_exist(matriz)

    


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
        procesar_archivo()
    elif numero == "3":
        print()
    elif numero == "4":
        Datos_estudiante()
    elif numero == "5":
        print("")
    elif numero == "6":
        print("salio de la aplicacion")
        ciclo = False