#Creado Por NeAnTime, Modulos Para Sofware Principal

def check_metasploit():
    try:
        subprocess.check_call(["which", "msfconsole"])
        subprocess.check_call(["which", "msfvenom"])
        return True
    except subprocess.CalledProcessError:
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