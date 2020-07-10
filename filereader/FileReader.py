#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""

import pandas as pd

from ConexionBD.CRUD.QrCode import QrCode
from entity.CodeQR import CodeQR


class FileReader:
    __route_file = ''
    __codeQRList = []
    __codeQRSaveList = []
    __codeQRUpdateList = []
    __qr_code_crud = any

    def __init__(self, route_file):
        self.__route_file = route_file
        self.__qr_code_crud = QrCode()

    def read_excel(self):
        excel_file = pd.read_excel(str(self.__route_file),
                                   names=['COD', 'REGISTRO', 'CEDULA', 'PROPIETARIO', 'ESTADO',
                                          'SITUACION', 'PLACA', 'CHASIS', 'ANIO',
                                          'MARCA', 'TIPO', 'OPERADORA', 'SERVICIO'])
        for i in range(len(excel_file)):
            code_qr = CodeQR(str(excel_file['COD'][i]).strip(), str(excel_file['REGISTRO'][i]).strip(),
                             str(excel_file['CEDULA'][i]).strip(), str(excel_file['PROPIETARIO'][i]).strip(),
                             str(excel_file['ESTADO'][i]).strip(), str(excel_file['SITUACION'][i]).strip(),
                             str(excel_file['PLACA'][i]).strip(), str(excel_file['CHASIS'][i]).strip(),
                             str(excel_file['ANIO'][i]).strip(), str(excel_file['MARCA'][i]).strip(),
                             str(excel_file['TIPO'][i]).strip(), str(excel_file['OPERADORA'][i]).strip(),
                             str(excel_file['SERVICIO'][i]).strip(), '')
            self.__codeQRList.append(code_qr)

    def code_action(self):
        code_list_ids = self.__qr_code_crud.find_shape_parent()
        for __codeQR in self.__codeQRList:
            exists_qr = 0
            for id_qr_code in code_list_ids:
                if str(id_qr_code) == str(__codeQR.reg):
                    exists_qr = 1
                    break
            if exists_qr == 1:

                self.__codeQRUpdateList.append(__codeQR)
            else:
                self.__codeQRSaveList.append(__codeQR)
        if len(self.__codeQRSaveList) > 0:
            print("PROCESS: EXISTEN DATOS A INGRESAR")
            self.__qr_code_crud.save_qr_code(self.__codeQRSaveList)
        if len(self.__codeQRUpdateList) > 0:
            print("PROCESS: EXISTEN DATOS A ACTUALIZAR")
            self.__qr_code_crud.update_qr_code(self.__codeQRUpdateList)
        self.__qr_code_crud.database_connection.close()


