from app.views.user_views import user_views


def register_blueprint(app):
    app.register_blueprint(user_views)