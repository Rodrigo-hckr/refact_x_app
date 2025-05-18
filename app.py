from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.models import db, init_db
from routes.routes import routes

app = Flask(__name__)

#--------------------------------------------------------------------configuracion db
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=SQLALCHEMY_TRACK_MODIFICATIONS


#---------------------------------------------inicizlizar db
db.init_app(app)
init_db(app)

#------------------------------------------------registro rutas
app.register_blueprint(routes)

#---------------------------ruta principal
@app.route('/')
def home():
    return '¡Bienvenido a la API de refacciones!'

#----------------------------------errores
@app.errorhandler(404)
def not_found(error):
    return {"error": "Ruta no encontrada"}, 404

@app.errorhandler(500)
def server_error(error):
    return {"error": "Error interno del servidor"}, 500

#-------------------------------------------------------------------------ejecucion     
if __name__ == "__main__":
    app.run(debug=True)    