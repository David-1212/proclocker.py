import time
import psutil
import subprocess

while True:
    for proc in psutil.process_iter():
        if proc.name() == 'main.exe':
            print('main Detectado')
            time.sleep(4)
        else:
            print('aplicacion no detectada.')
            time.sleep(4)

            op=int(input("Desea abrirla? /n 1.- si /n 2.-salir"))
            if op==1:
                p = subprocess.Popen('main.exe')
            elif op == 2:
                break
            else:
                print("opcion invalidaintente de nuevo con una opcion valida.")

        

        