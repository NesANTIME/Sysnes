#Creado Por NeAnTime, Modulos Para Sofware Principal

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

