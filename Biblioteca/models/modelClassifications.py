from app import db

class Clasificacion(db.Model):
    __tablename__ = 'clasificacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre_clasificacion = db.Column(db.String(50), unique=False)
    libros = db.relationship('Libros', backref="clasificaciones")
