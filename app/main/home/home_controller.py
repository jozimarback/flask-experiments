from flask_restplus import Resource, Namespace, fields
from flask import request

api = Namespace('Home',description='Home da API')
modelo = api.model('HomeModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'endereco': fields.String
})
@api.route('/')
class HomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return {"mensagem": "Home"}, 200
    @api.expect(modelo)
    def post(self):
        return request.json, 201

@api.route('/<id>')
class HomeIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id):
        return {"id": id, "nome": "Jozimar"}, 200

    @api.response(200, "Busca realizada com sucesso")
    @api.expect(modelo)
    def put(self, id):
        return {"id": id, "nome": request.args.get('nome'), "endereco": request.args.get('endereco')}, 201

    def delete(self, id):
        return {"mensagem": f"id {id} deletado com sucesso"}, 200
