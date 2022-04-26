#!/usr/bin/env python
'''
Heart DB manager
---------------------------
Autor: Ignacio Serrano
Version: 1.0

Descripcion:
Programa creado para administrar la base de datos de registro de Turnos
'''

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Turno(db.Model):
    __tablename__ = "turno"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    date = db.Column(db.DateTime)
       
    def __repr__(self):
        return f"Nombre:{self.name} con turno el dia {self.date}"

def insert(name, age, phone, date):
    person = Turno(name=name, age=age, phone=phone, date=date)
    db.session.add(person)
    db.session.commit()


def report(limit=0, offset=0):
    query = db.session.query(Turno)
    if limit > 0:
        query = query.limit(limit)
        if offset > 0:
            query = query.offset(offset)

    json_result_list = []

    for person in query:
        json_result = {'name': person.name, 'age': person.age, 'phone': person.phone, 'date': person.date}
        json_result_list.append(json_result)

    return json_result_list
    
def dashboard():
    query = db.session.query(Turno)
    n=0
    x = []
    y = []
    for person in query:
        y.append(person.age)
        x.append(person.id)
    return x, y

if __name__ == "__main__":
    print("Test del modulo heart.py")
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdatabase.db"
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    db.session.remove()
    db.drop_all()