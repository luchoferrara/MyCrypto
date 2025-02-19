from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import requests
import datetime


RUTA_MOVIMIENTOS = 1  # RUTA 1 = DB  - RUTA 0 = CSV

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={
    r'/api/*': {
        'origins': '*'
    }
})


@app.route('/convertir', methods=['POST'])
def convertir():
    if request.method == 'POST':
        tipo_transaccion = request.form['tipo_transaccion']
        from_moneda = request.form['from_moneda']
        to_moneda = request.form['to_moneda']
        cantidad_from = float(request.form['cantidad_from'])

        if tipo_transaccion == 'compra_eur_crypto':
            precio_unitario = obtener_precio('EUR', to_moneda)
            if precio_unitario:
                cantidad_to = cantidad_from / precio_unitario
                conn = get_db_connection()
                conn.execute('INSERT INTO transacciones (fecha_hora, tipo_transaccion, from_moneda, to_moneda, cantidad_from, cantidad_to, precio_unitario) VALUES (?, ?, ?, ?, ?, ?, ?)',
                             (datetime.datetime.now(), tipo_transaccion, from_moneda, to_moneda, cantidad_from, cantidad_to, precio_unitario))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
            else:
                return "Error al obtener el precio."

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
