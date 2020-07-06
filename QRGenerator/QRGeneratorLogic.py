#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
import pandas as pd
import pyqrcode
import base64
import uuid

from ConexionBD.CRUD.QrCode import QrCode
from entity.CodeQR import CodeQR


class QRGeneratorLogic:
    __route_file = ''
    __route_save_qr_image = ''
    __qr_string = ''
    __codeQRList = []

    def __init__(self, route_file, route_save_qr_image, qr_string):
        self.__route_file = route_file
        self.__route_save_qr_image = route_save_qr_image
        self.__qr_string = qr_string

    def read_excel(self):
        excel_file = pd.read_excel(str(self.__route_file),
                                   names=['COD', 'REG', 'CEDULA', 'PROPIETARIO', 'ESTADO',
                                          'SITUACION', 'PLACA', 'CHASIS', 'ANIO',
                                          'MARCA', 'TIPO', 'OPERADORA', 'SERVICIO'])
        for i in range(len(excel_file)):
            code_qr = CodeQR(str(excel_file['COD'][i]).strip(), str(excel_file['REG'][i]).strip(),
                             str(excel_file['CEDULA'][i]).strip(), str(excel_file['PROPIETARIO'][i]).strip(),
                             str(excel_file['ESTADO'][i]).strip(), str(excel_file['SITUACION'][i]).strip(),
                             str(excel_file['PLACA'][i]).strip(), str(excel_file['CHASIS'][i]).strip(),
                             str(excel_file['ANIO'][i]).strip(), str(excel_file['MARCA'][i]).strip(),
                             str(excel_file['TIPO'][i]).strip(), str(excel_file['OPERADORA'][i]).strip(),
                             str(excel_file['SERVICIO'][i]).strip(), '')
            self.__codeQRList.append(code_qr)

    def generate_qr_images(self):
        for i in range(len(self.__codeQRList)):
            url = pyqrcode.create(str(base64.b64encode(self.__codeQRList[i].get_str().encode("utf-8")), "utf-8"))
            self.__qr_string = str(self.__route_save_qr_image+'/' + str(uuid.uuid1()) + '.svg')
            url.svg(self.__qr_string, scale=8)
            self.__codeQRList[i].image_url = self.__qr_string

    def print_data(self):
        qr_code = QrCode()
        qr_code.save_qr_code(self.__codeQRList)

    def update_qr_image(self):
        url = pyqrcode.create(str(base64.b64encode(str(self.__qr_string).encode("utf-8")), "utf-8"))
        url.svg(self.__route_save_qr_image, scale=8)

