#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
import sys

from filereader.FileReader import FileReader
from qrgenerator.QRGenerator import QRGeneratorLogic


def start_qr_generator():
    print("PROCESS: Inicia Codigo Python")
    if str(sys.argv[1]) == str(1):
        route_file = str(sys.argv[2])
        generator = FileReader(route_file)
        generator.read_excel()
        generator.code_action()
    else:
        qr_generator = QRGeneratorLogic(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
        qr_generator.generate_qr_code()


if __name__ == "__main__":
    start_qr_generator()
