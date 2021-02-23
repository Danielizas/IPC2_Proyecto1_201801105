import os
clear = lambda: os.system('cls')


def cargar_archivo():
    print ("archivo cargado exitosamente")



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
        
        print("Archivo subido correctamente\n" " " )
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