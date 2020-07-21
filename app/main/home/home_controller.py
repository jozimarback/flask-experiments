from flask_restplus import Resource, Namespace

api = Namespace('Home',description='Home da API')

@api.route('/')
class HomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return {"mensagem": "Home"}, 200
