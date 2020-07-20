#!/usr/bin/python3

from ConexionBD.ConexionBD import database_connection


class ReportCancel:
    database_connection = ''

    def __init__(self):
        print("PROCESS: Llamado a Metodos CRUD PARA registrar Rutas")
        self.database_connection = database_connection

    def cancelReport(self, date_cancel):
        """
        Metodo Que registra en Nuestra BD un Objeto de Tipo Shape Parent
        :return: Retorna Un Objeto de Tipo Shape con su Id de BD
        """
        with database_connection.cursor() as cursor:
            try:
                save_point_query = 'update  user_report set     ' \
                                   '        dependency = ?, ' \
                                   '        status = ? ' \
                                   'where   CONVERT(datetime,fecha_registro,103) <= CONVERT(datetime,?,103);'
                cursor.execute(save_point_query, ('anulada','anulada', str(date_cancel)))
                cursor.commit()
                print("PROCESS: Shape Parent Registrado Correctamente")
            except Exception as e:
                print("PROCESS: Error al Registrar Shape Parent")
                cursor.rollback()
