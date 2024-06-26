#Creado Por NeAnTime, Modulos Para Sofware Principal
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


#____________________________________________________________________________________________________

def create_txt():
    rut_archivo = '.cache/'
    nombre = 'root.txt'

    try:
        ruta_completa = os.path.join(rut_archivo, nombre)
    
        with open(ruta_completa, 'w') as archivo:
            print(f"Archivo '{ruta_completa}', Registros Creados Exitosamente ")

    except Exception as e:
        print(f"Error al crear o escribir en el registro: {e}")




def Rel_tqdm():
    try:
        import tqdm
        return True
    except ImportError:
        return False
    
def Rel_metasploit():
    try:
        subprocess.check_call(["which", "msfconsole"])
        subprocess.check_call(["which", "msfvenom"])
        return True
    except subprocess.CalledProcessError:
        return False
    

def installer_metasploit():
    try:
        comando = "sudo apt install metasploit-framework"
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print("Metasploit se ha instalado correctamente.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar Metasploit: {e}")
        return False
    

def installer_tqdm():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])
        print("tqdm se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar tqdm: {e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")


def Submain(name, play):
    print(f"{name}, no se encuentra instalada..")
    od = input("¿Desea Instalarla Ahora? Y/N ")

    if od == "N" or "n":
        print("Error. No se Puede Continuar Con La Ejecucion del Playload")
        print("Descarge las Dependencias Requeridas. Error 80004001")
        input("Presione Enter Para Continuar... ")

    else:
        print(f"\nIniciando Descarga De la {play}...")
        installer_tqdm()
        if installer_tqdm():
            Barra(desc="Verificando La Instalacion:")
            print("\nSe Reiniciara El Payload, ¡Se Cerrara La Sesion!")
            input("Presione Enter Para Continuar... ")
            clear()
        
        else:
            print("La instalación falló. Error 710048005")



print("Verificando La Herramienta Metasploit ---")
print("Verificando la Dependencia MSFVenom\n")
Rel_metasploit()
reverse()

print("Verificando La Herramienta Python3 ---")
print("Verificando la Libreria tqdm\n")
Rel_tqdm()
reverse()

if not Rel_tqdm():
    Submain(name="La Libreria tqdm De Python", play="Libreria")

elif not Rel_metasploit():
    Submain(name="msfvenom - Metasploit", play="Dependencias")

else:
    print("Todas Las Herramientas y Dependencias Se Encuentran Instaladas...")
    create_txt()
    reverse()
    subprocess.run(['python', '../Sysnes.py'])

