from app.test.test_base import BaseTestCase

class PessoaTest(BaseTestCase):
    def test_pessoa_respondendo(self):
        response = self.client.get('/api/pessoa/1')
        self.assert200(response)
        self.assertEqual(response.json, {
            'id': 1,
            'nome': 'Jozimar Back',
            'endereco': 'Brasil'
        })