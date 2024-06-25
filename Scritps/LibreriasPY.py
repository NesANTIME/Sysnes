#Creado Por NeAnTime, Modulos Para Sofware Principal

def check_tqdm():
    try:
        import tqdm
        return True
    except ImportError:
        return False
    

    
def instalar_tqdm():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])
        print("tqdm se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar tqdm: {e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")