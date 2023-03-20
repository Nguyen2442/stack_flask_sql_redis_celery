from app.views.user_views import user_views
from app.views.file_views import file_views

def register_blueprint(app):
    app.register_blueprint(user_views)
    app.register_blueprint(file_views)