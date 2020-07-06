from ConexionBD.ConexionBD import database_connection


class QrCode:

    def __init__(self):
        print("PROCESS: Llamado a Metodos CRUD PARA registrar Rutas")
        self.database_connection = database_connection

    @staticmethod
    def save_qr_code(code_qr_list):
        with database_connection.cursor() as cursor:
            save_point_query = "INSERT INTO TransporteDMQ.dbo.qr_code ( " \
                               "anio_qr, cedula_qr, chasis_qr, codigo_qr, " \
                               "estado_qr, image_url_qr, marca_qr, operadora_qr, " \
                               "placa_qr, propietario_qr, reg_qr, servicio_qr, situacion_qr, tipo_qr) " \
                               "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

            records_to_insert = []
            for code_qr in code_qr_list:
                records_to_insert.append((str(code_qr.anio), str(code_qr.cedula), str(code_qr.chasis),
                                          str(code_qr.codigo), str(code_qr.estado), str(code_qr.image_url),
                                          str(code_qr.marca), str(code_qr.operadora), str(code_qr.placa),
                                          str(code_qr.propietario), str(code_qr.reg), str(code_qr.servicio),
                                          str(code_qr.situacion), str(code_qr.tipo)))
            try:
                cursor.executemany(save_point_query, records_to_insert)
                cursor.commit()
            except Exception as e:
                cursor.rollback()
                print("PROCESS: Error al Registrar Shape Parent" + str(e))
            finally:
                cursor.close()
