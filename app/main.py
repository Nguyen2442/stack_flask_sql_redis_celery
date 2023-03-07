from flask import (
    Flask, 
    jsonify
)
from app.blueprint import register_blueprint

# Function that create the app 
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    register_blueprint(app)

    # Simple route
    @app.route('/')
    def hello_world(): 
        return jsonify({
            "status": "success",
            "message": "Hello World!"
        }) 
    
    return app