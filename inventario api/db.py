import pymysql


def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='IngeCompu88?',
                                db='inventario')