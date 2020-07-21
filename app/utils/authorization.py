from functools import wraps
from flask import request, json
import requests

def verificar_usuario(token:str):
    url = 'autenticação'
    headers = {'Authorization': token }
    return requests.post(url, headers=headers)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return {'message': "Token não informado"}, 401
        r = verificar_usuario(token)
        try:
            response = json.loads(r.text)
            if response['codigo'] == "":
                raise PermissionError("Erro auth!")
        except Exception as ex:
            return {'message': f"Token expirado {ex}"}, 401
        return f(*args, **kwargs)
    return decorated
