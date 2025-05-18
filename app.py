from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.models import db, init_db

app = Flask(__name__)

#---------------------------------------------------------------------------------------------rutas
@app.route('/')
def home():
    return '¡Bienvenido a la API de Refacciones!'



app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
init_db(app)

    
if __name__ == "__main__":
    app.run(debug=True)    