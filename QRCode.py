#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
import sys

from QRGenerator import QRGeneratorLogic


def start_qr_generator():
    print("PROCESS: Inicia Codigo Python")
    route_file = str(sys.argv[1])
    route_save_qr_image = str(sys.argv[2])
    generator = QRGeneratorLogic.QRGeneratorLogic(route_file, route_save_qr_image, '')
    generator.read_excel()
    generator.code_action()


if __name__ == "__main__":
    start_qr_generator()
