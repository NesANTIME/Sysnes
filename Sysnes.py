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
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)

#-------------------------------------------------------------------------------------------------------------

def Opc_1():
    subprocess.run(['python', 'Tools/CreateAndroid.py'])
def Opc_2():
    print("No esta Disponible :(")

def Opc_3():
    rut = 'Scritps/cache/Acconts_sms/'
    archivo_txt = 'SMS_Cuentas.txt'
    ruta_txt = os.path.join(rut, archivo_txt)
    if os.path.exists(ruta_txt):
        print(f"\nComprobando Existencia De Cuentas en ({archivo_txt})")
        reverse(seg=2)
        print(f"Cuentas en {archivo_txt} ¡Existentes!")
        reverse(seg=1)
        with open(ruta_txt, 'r') as f:
            clear()
            Barra(desc="Cargando Datos...")
            subprocess.run(['python', 'Tools/SmsManager.py'])
    else:
        print(f"\nNo se Encontro la Existencia del archivo {archivo_txt}")
        print("A continuacion, Debera Registrar Una Cuenta API a Ultilizar...")
        reverse(seg=3)
        subprocess.run(['python', 'Scritps/Create_SmS_Twilio.py'])


#_____________________________________________________________________________________________________________

def Update():
    rut = 'Scritps/cache/'
    archivo_txt = 'root.txt'
    ruta_txt = os.path.join(rut, archivo_txt)

    Barra(desc="Analizando Paquetes...")

    if os.path.exists(ruta_txt):
        print("\nPaquetes cache existentes!")
        reverse(seg=1)
        print(f"\nComprobando Existencia De Archivo {archivo_txt}")
        reverse(seg=2)
        print(f"Archivo {archivo_txt} ¡Existente!")
        reverse(seg=1)
        with open(ruta_txt, 'r') as f:
            Main()

    else:
        print("\nEl payload se a ejecutado por primera vez...")
        print("Se Realizara Una Comprobacion de las Herramientas del Dispositivo...")
        reverse(seg=3)
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
    print("\nTodos Los Derechos Reservados (Version 1.5)\n")

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
        print("\n Creacion de Software (Version 1.0 Basic)")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print("1. Crear Archivo (.Apk)")
        print("2. Crear Archivo (.bat)")
        print("3. Atras\n")
        opc1 = int(input("--- Ingrese La Opcion: "))
        while (opc1 < 1) or (opc1 > 3):
            print("Error. La Opcion No esta Disponible :(")
            opc1 = int(input("--- Ingrese Nuevamente La Opcion: "))
        if opc1 == 1:
            clear()
            Opc_1()
        elif opc1 == 2:
            clear()
            Opc_2()
        else: 
            Main()

    elif (opc == 2):
        clear()
        print("\nEnvio de SMS (Version 1.0 Basic)")
        print("\n---------- ¿Que Operacion Desea Realizar? ----------\n")
        print("1. API Twilio (Debe Tener Una Cuenta En esta Plataforma)")
        print("2. ....")
        print("3. Atras\n")
        opc2 = int(input("--- Ingrese La Opcion: "))
        while (opc2 < 1) or (opc2 > 3):
            print("Error. La Opcion No esta Disponible :(")
            opc2 = int(input("--- Ingrese Nuevamente La Opcion: "))
        if opc2 == 1:
            clear()
            Opc_3()
        elif opc2 == 2:
            clear()
            Main()
        else: 
            Main()
            
    else:
        print("Programa Finalizado...")


def animation():
    clear()
    reverse(seg=0.2)
    print("INiciando.")
    reverse(seg=0.5)
    clear()
    print("inICiando..")
    reverse(seg=0.5)
    clear()
    print("inicIAndo...")
    reverse(seg=0.5)
    clear()
    print("iniciaNDo....")
    reverse(seg=0.5)
    clear()
    print("iniciandO....")
    reverse(seg=0.5)
    clear()


animation()
Update()
