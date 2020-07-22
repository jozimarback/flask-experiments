from flask_testing import TestCase
from app import app

class BaseTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
