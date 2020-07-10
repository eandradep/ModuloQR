from ConexionBD.ConexionBD import database_connection


def get_code_object_update(code_qr):
    return (str(code_qr.anio), str(code_qr.cedula), str(code_qr.chasis),
            str(code_qr.codigo), str(code_qr.estado), str(code_qr.marca),
            str(code_qr.operadora), str(code_qr.placa), str(code_qr.propietario),
            str(code_qr.reg), str(code_qr.servicio), str(code_qr.situacion),
            str(code_qr.tipo), str(code_qr.reg))


def get_code_object_save(code_qr):
    return (str(code_qr.anio), str(code_qr.cedula), str(code_qr.chasis),
            str(code_qr.codigo), str(code_qr.estado), str(code_qr.marca),
            str(code_qr.operadora), str(code_qr.placa), str(code_qr.propietario),
            str(code_qr.reg), str(code_qr.servicio), str(code_qr.situacion),
            str(code_qr.tipo))


class QrCode:
    database_connection = ''

    def __init__(self):
        print("PROCESS: Llamado a Metodos CRUD PARA registrar Rutas")
        self.database_connection = database_connection

    @staticmethod
    def save_qr_code(code_qr_list):
        with database_connection.cursor() as cursor:
            save_point_query = "INSERT INTO TransporteDMQ.dbo.qr_code ( " \
                               "anio_qr, cedula_qr , chasis_qr , " \
                               "codigo_qr , estado_qr ,  marca_qr , " \
                               "operadora_qr , placa_qr , propietario_qr , " \
                               "reg_qr , servicio_qr , situacion_qr , " \
                               "tipo_qr)  " \
                               "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
            records_to_insert = []
            try:
                for code_qr in code_qr_list:
                    records_to_insert.append(get_code_object_save(code_qr))
                cursor.executemany(save_point_query, records_to_insert)
                cursor.commit()
            except Exception as e:
                cursor.rollback()
                print("PROCESS: Error al Registrar Shape Parent" + str(e))


    @staticmethod
    def find_shape_parent():
        """
        Metodo Usado para Buscar un objeto de tipo Shape Parent por su nombre, una vez que encontramos el Registro en
        la BD, obtenes el Identificador de base de datos para poder registrar el detalle que serian la lista de
        puntos del Recorrido.
        :param id_qr_code:
        :return: Id del Objeto en la BD
        """
        code_list_ids = []
        with database_connection.cursor() as cursor:
            try:
                save_point_query = "select  reg_qr from qr_code;"
                cursor.execute(save_point_query)
                shape_parent_list = cursor.fetchall()
                for i in range(len(shape_parent_list)):
                    code_list_ids.append(shape_parent_list[i][0])
                print("PROCESS: QR ENCONTRADO")
                return code_list_ids
            except Exception as e:
                print("PROCESS: NO SE HA ENCONTRADO QR")
                return False

    @staticmethod
    def update_qr_code(code_qr_list):
        with database_connection.cursor() as cursor:
            save_point_query = "UPDATE TransporteDMQ.dbo.qr_code SET     " \
                               "anio_qr = ?, cedula_qr = ?, chasis_qr = ?, " \
                               "codigo_qr = ?, estado_qr = ?,  marca_qr = ?, " \
                               "operadora_qr = ?, placa_qr = ?, propietario_qr = ?, " \
                               "reg_qr = ?, servicio_qr = ?, situacion_qr = ?, " \
                               "tipo_qr = ? " \
                               "WHERE reg_qr = ?;"

            records_to_insert = []
            try:
                for code_qr in code_qr_list:
                    records_to_insert.append(get_code_object_update(code_qr))
                cursor.executemany(save_point_query, records_to_insert)
                cursor.commit()
            except Exception as e:
                cursor.rollback()
                print("PROCESS: Error al ACTUALIZAR DATOS Shape Parent" + str(e))
