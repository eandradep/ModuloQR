#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""

import pyodbc

# __server_address = '192.168.0.108\SQLEXPRESS,1433'
# __database_name = 'TransporteDMQ'
# __database_user_name = 'sa'
# __database_user_password = 'patito123456Ab'


__server_address = '54.90.120.82\SQLEXPRESS,1433'
__database_name = 'TransporteDMQ'
__database_user_name = 'sa'
__database_user_password = 'patito123456Ab'

try:
    database_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + __server_address
                                         + ';DATABASE=' + __database_name
                                         + ';UID=' + __database_user_name
                                         + ';PWD=' + __database_user_password)
    print("PROCESS: Conecta con La BD")
except Exception as e:
    print("PROCESS: Ocurrió un error al conectar a SQL Server: " + str(e))