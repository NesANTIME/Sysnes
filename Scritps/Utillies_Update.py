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
def reverse(seg):
    time.sleep(seg)
def Barra(desc):
    lista_de_elementos = range(100)
    for elemento in tqdm(lista_de_elementos, desc):
        time.sleep(0.1)


#____________________________________________________________________________________________________

def create_txt():
    subprocess.run(['python', 'Scritps/cache/data_temporal.py'])

def Utilios():
    subprocess.run(['python', 'Scritps/Utillies_Update.py'])

def Rel_tqdm():
    try:
        import tqdm
        return True
    except ImportError:
        return False
    
def Rel_pip():
    try:
        subprocess.check_call(['dpkg', '-s', "python3-pip"])
        return True
    except subprocess.CalledProcessError:
        return False 
    
def Rel_Twilio():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'show', 'twilio'])
        return True
    except subprocess.CalledProcessError:
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
        Utilios()
        return False
    
    
def installer_pip():
    try:
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'python3-pip'])
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'python3-pip'])
        print("pip se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar pip: {e}")
        Utilios()
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
        Utilios()

def installer_Twilio():
    try:
        print("Se Iniciara La Instalacion...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'twilio'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'twilio'])
        clear()
        print("La Instalacion de Twilio se Completo Correctamente...")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar Twilio: {e}")
        Utilios()
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
        Utilios()
    

def installer_tqdm():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])
        print("tqdm se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar tqdm: {e}")
        Utilios()
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
        Utilios()


def Submain(name, play):
    print(f"{name}, no se encuentra instalada..")
    od = input("¿Desea Instalarla Ahora? Y/N ")

    if od == "N" or "n":
        print("Error. No se Puede Continuar Con La Ejecucion del Playload")
        print("Descarge las Dependencias Requeridas. Error 80004001")
        input("Presione Enter Para Continuar... ")

    else:
        print(f"\nIniciando Descarga De la {play}...")




print("Verificando La Herramienta Metasploit ---")
print("Verificando la Dependencia MSFVenom\n")
Rel_metasploit()
reverse(seg=1)

print("Verificando La Herramienta Python3 ---")
print("Verificando la Libreria tqdm\n")
Rel_tqdm()
print("\nVerificando la Libreria pip\n")
Rel_pip()
print("Verificando la libreria Twilio\n")
Rel_Twilio()
reverse(seg=2)

if not Rel_tqdm():
    Submain(name="La Libreria tqdm De Python", play="Libreria")
    installer_tqdm()
    if installer_tqdm():
            Barra(desc="Verificando La Instalacion:")
            print("\nSe Reiniciara El Payload...")
            reverse(seg=2)
            subprocess.run(['python', 'Sysnes.py'])
            clear()
    else:
        print("La instalación falló. Error 710048005")


elif not Rel_pip():
    Submain(name="La Libreria pip De Python", play="Libreria")
    installer_pip()
    if installer_pip():
            Barra(desc="Verificando La Instalacion:")
            print("\nSe Reiniciara El Payload...")
            reverse(seg=2)
            subprocess.run(['python', 'Sysnes.py'])
            clear()
    else:
        print("La instalación falló. Error 710048005")


elif not Rel_Twilio():
    Submain(name="La Libreria Twilio De Python", play="Libreria")
    installer_Twilio()
    if installer_Twilio():
            Barra(desc="Verificando La Instalacion:")
            print("\nSe Reiniciara El Payload...")
            reverse(seg=2)
            subprocess.run(['python', 'Sysnes.py'])
            clear()
    else:
        print("La instalación falló. Error 710048005")


elif not Rel_metasploit():
    Submain(name="msfvenom - Metasploit", play="Dependencia")
    installer_metasploit()
    if installer_metasploit():
            Barra(desc="Verificando La Instalacion:")
            print("\nSe Reiniciara El Payload...")
            reverse(seg=2)
            subprocess.run(['python', 'Sysnes.py'])
            clear()
    else:
        print("La instalación falló. Error 710048005")


else:
    print("Todas Las Herramientas y Dependencias Se Encuentran Instaladas...")
    create_txt()
    reverse(seg=1)
    print("Iniciando el Payload...")
    subprocess.run(['python', 'Sysnes.py'])
