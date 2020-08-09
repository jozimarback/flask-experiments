from flask_restplus import Resource, Namespace

api = Namespace('Home',description='Home da API')

@api.route('/')
class HomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return {"mensagem": "Home"}, 200
    def post(self):
        pass

@api.route('/<id>')
class HomeIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id):
        return {"mensagem": "Home"}, 200

    @api.response(200, "Busca realizada com sucesso")
    def put(self, id):
        return {"mensagem": "Home"}, 200

