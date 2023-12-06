from flask import Flask
from app.routes import bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234'  
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
