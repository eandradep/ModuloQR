"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""


class CodeQR:
    """
    Objeto Forma Punto, contiene los valores minimos para especificar la informacion de un Punto
    en el mapa.
    """

    codigo = ''
    reg = ''
    cedula = ''
    propietario = ''
    estado = ''
    situacion = ''
    placa = ''
    chasis = ''
    anio = ''
    marca = ''
    tipo = ''
    operadora = ''
    servicio = ''
    image_url = ''

    def __init__(self, codigo, reg, cedula,
                 propietario,estado, situacion,
                 placa, chasis, anio,
                 marca, tipo, operadora, servicio, image_url):
        self.codigo = codigo
        self.reg = reg
        self.cedula = cedula
        self.propietario = propietario
        self.estado = estado
        self.situacion = situacion
        self.placa = placa
        self.chasis = chasis
        self.anio = anio
        self.marca = marca
        self.tipo = tipo
        self.operadora = operadora
        self.servicio = servicio
        self.image_url = image_url
