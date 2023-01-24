from flask import Flask
# Para solucionar el problema del Cross Origin
# Que el front no pueda acceder al back
from flask_cors import CORS 
from flask import jsonify
from db import obtener_conexion
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    conexion = obtener_conexion()

    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idProducto, nombre, precio, stock FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return jsonify(productos)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()