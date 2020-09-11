from app import app
from models.modelClassifications import *
from models.modelBooks import *
from flask import render_template, request, url_for, redirect, jsonify

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getAllBook')
def getAll():
    libros = Libros.query.all()
    return render_template('index.html', list = libros)

@app.route('/getOneBook', methods=['POST'])
def getOne():
    libro_solicitado=request.form['libro']
    libro_retornado = Libros.query.filter_by(titulo = libro_solicitado).first()

    if (libro_retornado is None):
        return render_template('index.html', lista = "No encontrado")
    else:
        clasificacion_retornado = Clasificacion.query.filter_by(id = libro_retornado.clasificacion_id).first()
        return render_template('index.html', lista = [[libro_retornado.titulo, libro_retornado.autor, clasificacion_retornado.nombre_clasificacion]])

@app.route('/createBook', methods=['POST'])
def create():
    nuevo_libro = Libros(titulo=request.form['titulo'], autor=request.form['autor'], clasificacion_id=request.form['clasificacion_id'])
    db.session.add(nuevo_libro)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/deleteBook/<id>', methods = ['POST'])
def deleteBook(id):
    print (id)
    Libros.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return "Eliminado!"

@app.route('/updateBook', methods = ['GET', 'POST'])
def update():
    datos = Libros.query.get(request.form.get('id'))
    datos.titulo = request.form['titulo']
    datos.autor = request.form['autor']
    datos.clasificacion_id = request.form['clasificacion_id']
    db.session.commit()
    return "Updated!"
