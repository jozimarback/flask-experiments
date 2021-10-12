from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.pessoa.pessoa_controller import api as home_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

authorizations = {
    'bearer': {
        'name': "Authorization",
        'in': "header",
        'type': "apiKey",
        'description': "Insert your JWT Token here!"
    }
}
api = Api(app, title='Flask Experiments Api', version='1.0', description='Experiments with python flask',prefix='/api', authorizations=authorizations)


api.add_namespace(home_ns, path='/person')