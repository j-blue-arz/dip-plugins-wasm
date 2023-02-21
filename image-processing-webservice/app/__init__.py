import os

from flask import Flask


def create_app():
    app = Flask(
        __name__,
        static_folder="../../webclient",
        static_url_path="",
        instance_relative_config=True,
    )
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import image_service

    app.register_blueprint(image_service.API)

    @app.route('/')
    def index():
        return app.send_static_file("index.html")

    return app