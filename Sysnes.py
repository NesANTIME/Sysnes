#Programa Creado Por NesAnTime
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
    else:
        print("Este Sistema No Posee Mas Soporte")
def reverse():
    seg = 3
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)

def Opc_1():
    subprocess.run(['python', 'Tools/CreateAndroid.py'])



def Update():
    rut = 'Scritps/.cache/'
    archivo_txt = 'root.txt'
    
    ruta_txt = os.path.join(rut, archivo_txt)

    if os.path.exists(ruta_txt):
        print(f"Comprobando Los Archivos {archivo_txt} existentes.")
        reverse()
        with open(ruta_txt, 'r') as f:
            Opc_1()


    else:
        print("El Payload Es Ejecutado Por Primera Vez, Se Realizara Una Comprobacion de las Herramientas Compatibles")
        reverse()
        subprocess.run(['python', 'Scritps/Utillies_Update.py'])




def Main():
    clear()
    print("\nPyload Creado Por NesAnTime\n")
    print("  ██████▓██   ██▓  ██████  ███▄    █ ▓█████   ██████")
    print("▒██    ▒ ▒██  ██▒▒██    ▒  ██ ▀█   █ ▓█   ▀ ▒██    ▒")
    print("░ ▓██▄    ▒██ ██░░ ▓██▄   ▓██  ▀█ ██▒▒███   ░ ▓██▄  ")
    print("  ▒   ██▒ ░ ▐██▓░  ▒   ██▒▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒")
    print("▒██████▒▒ ░ ██▒▓░▒██████▒▒▒██░   ▓██░░▒████▒▒██████▒▒")
    print("▒ ▒▓▒ ▒ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░")
    print("░ ░▒  ░ ░▓██ ░▒░ ░ ░▒  ░ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░")
    print("░  ░  ░  ▒ ▒ ░░  ░  ░  ░     ░   ░ ░    ░   ░  ░  ░  ")
    print("      ░  ░ ░           ░           ░    ░  ░      ░  ")
    print("         ░ ░                                         ")
    print("\nTodos Los Derechos Reservados (Version 1.3)\n")

    print("__________ Menu De Opciones __________")
    print("1. Crear Software (Reverb Shell)")
    print("2. Num Spam (SMS, CORREO)")
    print("3. Cerrar Sysnes\n")
    opc = int(input("-- Ingrese La Opcion: "))
    while (opc < 1) or (opc > 3):
        print("Error. La Opcion No esta Disponible :(")
        opc = int(input("-- Ingrese Nuevamente La Opcion: "))

    if (opc == 1):
        clear()
        print("\n Creacion de Software (Version 1.2)\n")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print("1. Crear Archivo (.Apk) (Alfha v1)")
        print("2. Crear Archivo (.Exe o .msi) (Beta v-0)")
        print("3. Crear Comando PowerShell (Windows) (Beta v-0)")
        print("4. Atras\n")
        opc1 = int(input("--- Ingrese La Opcion: "))
        while (opc1 < 1) or (opc1 > 4):
            print("Error. La Opcion No esta Disponible :(")
            opc1 = int(input("--- Ingrese Nuevamente La Opcion: "))
        if opc1 == 1:
            clear()
            Update()
        elif opc1 == 2:
            print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
        elif opc1 == 3:
            print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
        else: 
            Main()

    elif (opc == 2):
        print("Modo En Desarrallo :) ")
        print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
        input()
        Main()

    else:
        print("Programa Finalizado...")


print("Iniciando...")
input("\nPresione Enter Para Continuar...")
Main()



