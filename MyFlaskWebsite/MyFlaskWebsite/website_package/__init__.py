from flask import Flask
import os

UPLOAD_FOLDER =os.path.dirname(os.path.abspath(__file__)) 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "yolo"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    from .views import views
    from .auth import auth
    from .prediction import pred
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(pred, url_prefix='/')
    
    return app
