from flask import Flask
from app.users.routes import userAPI
from app.products.routes import productsAPI

def createApp():
    app = Flask(__name__)
    app.register_blueprint(userAPI)
    app.register_blueprint(productsAPI)
    
    return app