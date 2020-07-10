#!/usr/bin/python3
import subprocess
import sys

list_files = subprocess.run(["/usr/bin/python3",
                             sys.argv[1]+"/ModuloQR/QRCode.py",  # DIreccion del codigo que incia el proceso
                             sys.argv[2],   # Tipo de proceso
                             sys.argv[3],   # Direccion en donde se encuentra el archivo xls // direccion de la Imagen
                             sys.argv[4],   # codigo_registro
                             sys.argv[5]])  # texto emcriptado
