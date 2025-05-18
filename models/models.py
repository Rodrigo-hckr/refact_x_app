from flask import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
    
class Refaccionaria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    direccion = db.Column(db.String(200))
    suscripcion_activa = db.Column(db.Boolean, default=True)
    
class Cotizacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db. ForeignKey('usuario.id'), nullable=False)
    refaccion = db.Column(db.String(200), nullable=False)
    fecha_solicitud = db.Column(db.DateTime, default=db.func.current_timestamp())
    
class RespuestaCotizacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cotizacion_id = db.Column(db.Integer, db.ForeignKey('cotizacion.id'), nullable=False)
    refaccionaria_id = db.Column(db.Integer, db.ForeignKey('refaccionaria.id'), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    fecha_respuesta = db.Column(db.DateTime, default=db.func.current_timestamp())    
            