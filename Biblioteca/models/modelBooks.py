from app import db

class Libros(db.Model):
    __tablename__ = 'libros'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    clasificacion_id = db.Column(db.Integer, db.ForeignKey('clasificacion.id'), nullable=False)