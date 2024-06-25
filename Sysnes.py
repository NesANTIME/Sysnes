#Programa Creado Por NesAnTime
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys

def clear():
    from Scritps.Animations import Limpiar
    Limpiar()
def reverse():
    from Scritps.Animations import lapzo
    lapzo()
def Barra(desc):
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)



def RelMetasploit():
   from Scritps.Metasploit import check_metasploit
   check_metasploit()
    
def Reltqdm():
    from Scritps.LibreriasPY import check_tqdm
    check_tqdm()
    
def installerMetasploit():
    from Scritps.Metasploit import instalar_metasploit
    instalar_metasploit()
    
def installertqdm():
    from Scritps.LibreriasPY import instalar_tqdm
    instalar_tqdm()
    


def ChequerUpdate():
    print("Comprobando dependencias Instaladas ---")
    reverse()

    print("Verificando La Herramienta Metasploit ---")
    RelMetasploit()
    reverse()

    print("Verificando la Dependencia MSFVenom ---")
    reverse()
    
    print("Verificando la Libreria tqdm ---")
    Reltqdm()

    if (not Reltqdm()) or (not RelMetasploit()):
        if not Reltqdm():
            print("La Libreria de Python tqdm, no se encuentra instalada..")
            od = input("¿Desea Instalarla Ahora? Y/N ")
            if od == "N" or "n":
                print("Error. No se Puede Continuar Con La Ejecucion del Playload")
                print("Descarge las Dependencias Requeridas. Error 80004001")
                input("Presione Enter Para Continuar... ")
                
            else:
                print("Iniciando Descarga De la Libreria...")
                installertqdm()
                if installertqdm():
                    Barra(desc="Verificando La Instalacion:")
                    print("Se Puede Proceder Con La Ejecucion del Playload")
                    input("Presione Enter Para Continuar... ")
                    clear()
                    ChequerUpdate()
                else:
                    print("La instalación de Metasploit falló. Error 710048005")
        
        elif not RelMetasploit():
            print("msfvenom - Metasploit no está instalado en el sistema.")
            opd = input("¿Desea Instalarlo Ahora? Y/N ")
            if opd == "N" or "n":
                print("Error. No se Puede Continuar Con La Ejecucion del Playload")
                print("Descarge las Dependencias Requeridas. Error 80004001")
                input("Presione Enter Para Continuar... ")
            else:
                print("Iniciando Descarga De Dependencias...")
                installerMetasploit()
                if installerMetasploit():
                    Barra(desc="Verificando La Instalacion:")
                    print("\nAhora puedes utilizar Metasploit.")
                    print("Se Puede Proceder Con La Ejecucion del Playload")
                    input("Presione Enter Para Continuar... ")
                    clear()
                    ChequerUpdate()
                else:
                    print("La instalación de Metasploit falló. Error 710048005")

    else:
        print("Todas Las Librerias Y Dependencias Estan Corretamente Habilitadas")
        print("Se Puede Proceder con la Ejecucion del Payload")
        reverse()
        

    
def Opc_1():
    from Tools.CreateAndroid import ToolCreatorAndroid
    ToolCreatorAndroid()


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
    print("\nTodos Los Derechos Reservados (Version 1.24)\n")

    print("__________ Menu De Opciones __________")
    print("1. Crear Software (Reverb Shell)")
    print("2. Iniciar Modo ROOT (En Espera de Reverb Shell)\n")
    print("3. Cerrar Sysnes")
    opc = int(input("Ingrese La Opcion: "))
    while (opc < 1) or (opc > 3):
        print("Error. La Opcion No esta Disponible :(")
        opc = int(input("Ingrese Nuevamente La Opcion: "))

    if (opc == 1):
        print(" Creacion de Software (Version 1.2)\n")
        print("\n")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print("1. Crear Archivo (.Apk) (Alfha v1)")
        print("2. Crear Archivo (.Exe o .msi) (Beta v-0)")
        print("3. Crear Comando PowerShell (Windows) (Beta v-0)")
        print("4. Atras\n")
        opc1 = int(input("Ingrese La Opcion: "))
        while (opc1 < 1) or (opc1 > 4):
            print("Error. La Opcion No esta Disponible :(")
            opc1 = int(input("Ingrese Nuevamente La Opcion: "))
        if opc1 == 1:
            clear()
            Opc_1()
        elif opc1 == 2:
            print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
        elif opc1 == 3:
            print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
        else: 
            Main()

    elif (opc == 2):
        print("Modo En Desarrallo :) ")
        input()
        Main()

    else:
        print("Programa Finalizado...")


print("Iniciando...")
input("\nPresione Enter Para Continuar...")
Main()



