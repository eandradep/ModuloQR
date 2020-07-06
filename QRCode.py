#!/usr/bin/python3

import pandas as pd
import hashlib
import pyqrcode
import base64
from entity.CodeQR import CodeQR


def encrypt_string(hash_string):
    return hashlib.sha1(hash_string.encode()).hexdigest()


def get_qr_code(code_qr_entity):
    url = pyqrcode.create(str(base64.b64encode(code_qr_entity.get_str().encode("utf-8")), "utf-8"))
    url.svg(code_qr_entity.cedula + '-' + code_qr_entity.placa + '-' + code_qr_entity.operadora+'.svg', scale=8)


df = pd.read_excel("/home/edisonandrade/Downloads/registros_municipales.xls",
                   names=['COD', 'REG', 'CEDULA', 'PROPIETARIO', 'ESTADO',
                          'SITUACION', 'PLACA', 'CHASIS', 'ANIO',
                          'MARCA', 'TIPO', 'OPERADORA', 'SERVICIO'])

CodeQRList = []
for i in range(len(df)):
    codeQR = CodeQR(str(df['COD'][i]).strip(), str(df['REG'][i]).strip(), str(df['CEDULA'][i]).strip(),
                    str(df['PROPIETARIO'][i]).strip(), str(df['ESTADO'][i]).strip(), str(df['SITUACION'][i]).strip(),
                    str(df['PLACA'][i]).strip(), str(df['CHASIS'][i]).strip(), str(df['ANIO'][i]).strip(),
                    str(df['MARCA'][i]).strip(), str(df['TIPO'][i]).strip(), str(df['OPERADORA'][i]).strip(),
                    str(df['SERVICIO'][i]).strip())
    sha_signature = encrypt_string(str(codeQR.get_str()))
    CodeQRList.append(codeQR)

get_qr_code(CodeQRList[3])
get_qr_code(CodeQRList[5])
get_qr_code(CodeQRList[8])

# CLIENTE : 1
# CONTROLADOR : 2
# AGENTE : 3
