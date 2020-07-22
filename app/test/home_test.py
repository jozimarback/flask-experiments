from app.test.test_base import BaseTestCase

class HomeTes(BaseTestCase):
    def test_home_responding(self):
        response = self.client.get('/api/home/')
        self.assert200(response)
        self.assertEqual(response.json, {"mensagem": "Home"})