#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
import sys

from ConexionBD.CRUD.ReportCancel import ReportCancel
from filereader.FileReader import FileReader
from filezip.CompressFile import CompressFile
from qrgenerator.QRGenerator import QRGeneratorLogic


def start_qr_generator():
    print("PROCESS: Inicia Codigo Python")
    if str(sys.argv[1]) == str(1):
        route_file = str(sys.argv[2])
        generator = FileReader(route_file)
        generator.read_excel()
        generator.code_action()
    if str(sys.argv[1]) == str(2):
        qr_generator = QRGeneratorLogic(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
        qr_generator.generate_qr_code()
    if str(sys.argv[1]) == str(3):
        compress_file = CompressFile(str(sys.argv[2]), str(sys.argv[3]))
        compress_file.generate_zip_file()
    if str(sys.argv[1]) == str(4):
        report = ReportCancel()
        report.cancelReport(str(sys.argv[2]))
    FileReader('').close_connection()


if __name__ == "__main__":
    start_qr_generator()
