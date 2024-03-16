from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    from apps import views as main_views

    app.register_blueprint(main_views.bp, url_prefix="/")

    from apps.auth import views as auth_views

    app.register_blueprint(auth_views.bp, url_prefix="/auth")

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    return app


def page_not_found(e):
    """404 Not Found"""
    return render_template("404.html"), 404


def internal_server_error(e):
    """500 Internal Server Error"""
    return render_template("500.html"), 500
