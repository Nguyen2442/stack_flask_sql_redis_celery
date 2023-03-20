from flask import (
    Flask, 
    jsonify
)
from app.blueprint import register_blueprint
from app.core.database.base import setup_db


# Function that create the app 
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    register_blueprint(app)

    setup_db(app)

    # Simple route
    @app.route('/')
    def hello_world(): 
        return jsonify({
            "status": "success",
            "message": "Hello World!"
        }) 
    
    return app