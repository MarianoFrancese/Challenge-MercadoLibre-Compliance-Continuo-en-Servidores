import os
import platform
import psutil
import requests
import json

url = "http://127.0.0.1:5000/"

infosistema = {
    "InfoProcesador" : platform.processor(), #info del procesador
    "Procesos" : os.popen('ls -la').read, #procesos corriendo
    "Usuarios" : psutil.users(), #usuarios conectados
    "VersionSO" : os.uname().version, #version del sistema operativo
    "NombreSO" : os.uname().sysname #nombre del sistema operativo
}

informacion = json.dumps(infosistema)

response = requests.post(url, informacion)
