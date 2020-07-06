#!/usr/bin/python3
import subprocess
import sys

list_files = subprocess.run(["/usr/bin/python3",
                             sys.argv[1]+"/ModuloQR/QRCode.py",  # DIreccion del codigo que incia el proceso
                             sys.argv[2],   # Tipo de proceso
                             sys.argv[3],   # Direccion en donde se encuentra el archivo xls // string con texto
                             sys.argv[4]])  # Direccion en donde se van a almacenar los Codigos QR
