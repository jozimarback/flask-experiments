from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.pessoa.pessoa_db import PessoaDb

api = Namespace('Pessoa',description='Manutenção dados de pessoa')
modelo = api.model('PessoaModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'endereco': fields.String
})
@api.route('/')
class PessoaController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return PessoaDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return PessoaDb.adicionar(request.json), 201

@api.route('/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return PessoaDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome da pessoa')
    @api.param('endereco','Endereço da pessoa')
    def put(self, id:int):
        return PessoaDb.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return PessoaDb.remover(int(id)), 200
