 #Creado Por NeAnTime, Modulos Para Sofware Principal
from tqdm import tqdm
import os
import subprocess
import platform
import time
import sys

#----------------------------------------------------------------------------------

def create_root_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'root.txt')
    with open(file_path, 'w') as file:
        file.write("03358440-0e66-4adb-862d-6df7f106f4c2-XGMS7e7n2sdX-NOWGuMKBIGel-yt2Xp7ov4m6e-633oMKM5Qrle-CwtWlf0ZyPXm-NIXZFgWcSh97-tYj1NwfrmmTP-GrbSRoxhq9VW-H0TBJzTQpgC7-B6WosSV0i8tC-URaKozETAZ-3vOonS2bf4MT-5uINQmRlgtgF-b9IQssMEz7jH9di2OMoD2t9uBP7LOQ-WhIC1ryNRaG4-aSRG5J71UoIZ-AicmG5kQUP6z- 5mfLX45UDqrk - Nesantime - Sysnes :)")
    print(f"Archivo de Registro y cache 'root.txt' creado ¡exitosamente!")
create_root_file()
