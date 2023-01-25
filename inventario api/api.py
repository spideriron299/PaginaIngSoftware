from flask import Flask
# Para solucionar el problema del Cross Origin
# Que el front no pueda acceder al back
from flask_cors import CORS
from flask import jsonify
from db import obtener_conexion

app = Flask(__name__)
CORS(app)

@app.route('/')

def hello_world():
    conexion = obtener_conexion()

    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idProducto, nombre, precio, stock FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return jsonify(productos)


if __name__ == '__main__':

    app.run()