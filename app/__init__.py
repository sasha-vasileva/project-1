from flask import Flask, request
from flask_babel import Babel, gettext

babel = Babel()


def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)

    # стандартная конфигурация
    app.config.from_object('app.config.Config')
    if config_object:
        app.config.update(config_object)

    # инициализация расширений
    babel.init_app(app)

    @app.context_processor
    def inject_conf():
        return dict(gettext=gettext)

    # регистрируем роуты
    from .routes import main_bp

    app.register_blueprint(main_bp)

    return app
