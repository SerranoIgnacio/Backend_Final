'''
Flask [Python]
Ejercicios de práctica

Autor: Inove Coding School
Version: 2.0
 
Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
las turnos registradas.

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''

# Realizar HTTP POST con --> post.py

from datetime import datetime
import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from turno import Turno

import utils
import turno

app = Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///turnos.db"
# Asociamos nuestro controlador de la base de datos con la aplicacion
turno.db.init_app(app)


@app.route("/")
def index():
    try:
        print("Renderizar index.html")
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/turnos")
def turnos():
    try:
        limit_str = str(request.args.get('limit'))
        offset_str = str(request.args.get('offset'))

        limit = 0
        offset = 0

        if(limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)

        if(offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)

        data = turno.report(limit, offset)
        
        result = render_template('tabla.html', data=data)
      
        return result
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        try:
            return render_template('registro.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            name = ""
            age = 0
            phone = 0
            date = datetime

            name = str(request.form.get('name')).lower()
            age = str(request.form.get('age'))
            phone = str(request.form.get('phone'))
            date_str = str(request.form.get('date'))
            date = datetime.strptime(date_str, '%Y-%m-%d')
            turno.insert(name, int(age), int(phone), date)
            
            return redirect(url_for('turnos'))
        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/comparativa")
def comparativa():
    try:
        x, y = turno.dashboard()
        image_html = utils.graficar(x, y)
        return Response(image_html.getvalue(), mimetype='image/png')
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.before_first_request
def before_first_request_func():
    turno.db.create_all()
    print("Base de datos generada")

if __name__ == '__main__':
    print('Inove@Server start!')
    app.run(host="127.0.0.1", port=5000)
