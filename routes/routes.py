from flask import Blueprint, request, jsonify
from models.models import db, Usuario, Refaccionaria, Cotizacion, RespuestaCotizacion

routes = Blueprint('routes', __name__)

@routes.route('/register-user', methods=['POST'])
def register_user():
    data = request.json
    new_user = Usuario(nombre=data['nombre'], telefono=data['telefono'], correo=data['correo'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuario registrdo correctamente"})

@routes.route('/register-refaccionaria', methods=['POST'])
def register_refaccionaria():
    data = request.json
    new_refaccionaria = Refaccionaria(nombre=data['nombre'], telefono=data['telefono'], correo=data['correo'])
    db.session.add(new_refaccionaria)
    db.session.commit()
    return jsonify({"message": "Refaccionaria registrada correctamente"})

@routes.route('/quote-request', methods=['POST'])
def request_quote():
    data = request.json
    new_quote = Cotizacion(usuario_id=data['usuario_id'], refaccion=data['refaccion'])
    db.session.add(new_quote)
    db.session.commit()
    return jsonify({"message": "Cotización enviada a refaccionarias"})

@routes.route('/quote-response', methods=['POST'])
def quote_response():
    data = request.json
    new_response = RespuestaCotizacion(cotizacion_id=data['cotizacion_id'], refaccionaria_id=data['refaccionaria_id'], precio=data['precio'])
    db.session.add(new_response)
    db.session.commit()
    return jsonify({"message": "Respuesta de cotizacion registrada"})

@routes.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = RespuestaCotizacion.query.order_by(RespuestaCotizacion.precio.asc()).all()
    return jsonify([{"cotizacion_id": q.cotizacion_id, "refaccionaria_id": q.refaccionaria_id, "precio": q.precio} for q in quotes])