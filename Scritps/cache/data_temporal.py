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

#----------------------------------------------------------------------------------
def create_root_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'root.txt')

    with open(file_path, 'w') as file:
        file.write("03358440-0e66-4adb-862d-6df7f106f4c2 - Nesantime - Sysnes :)")
    
    print(f"Archivo 'root.txt' creado en: {file_path} ¡Exitosamente! ;)")

create_root_file()

