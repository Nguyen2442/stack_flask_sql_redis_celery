import os
from app.config import settings
from app.main import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    gunicorn_app = create_app()