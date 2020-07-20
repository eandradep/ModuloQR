#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""

import zipfile
import os
from os.path import basename, isfile
from os import listdir


class CompressFile:
    __file_path__ = ''
    __save_location__ = ''
    __file_list__ = []

    def __init__(self, __file_path__, __file__):
        print("PROCESS: Inicia proceso de generacion de gtfs")
        self.__file_path__ = str(__file_path__) + '' + str(__file__)
        self.__save_location__ = __file_path__
        for obj in self.list_files():
            if str(obj).split('.')[1] == 'png':
                if str(obj).split('.')[0].find("-eps") >= 0:
                    print('NO SE AGREGA')
                else:
                    self.__file_list__.append(self.__file_path__ + '' + str(obj))


    def generate_zip_file(self):
        compression = zipfile.ZIP_DEFLATED
        file_name = self.__save_location__+"ALLQRCODE.zip"
        os.remove(str(file_name))
        zf = zipfile.ZipFile(file_name, mode="w")
        try:
            for filename in self.__file_list__:
                zf.write(str(filename), basename(str(filename)), compress_type=compression)
        finally:
            zf.close()
        print("PROCESS:", file_name)

    def list_files(self):
        return [obj for obj in listdir(self.__file_path__) if isfile(self.__file_path__ + obj)]
