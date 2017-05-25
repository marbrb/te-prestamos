from uuid import uuid4
from queries import registrar_cookie, obtener_cliente
from tornado import web
import json


class BaseHandler(web.RequestHandler):
    def get_current_user(self):
        if obtener_cliente(self.get_secure_cookie("logged")):
            return 1
        else:
            return 0

class LoginHandler(BaseHandler):
    def post(self):
        #diccionario para accesar al JSON
        try:
            data = json.loads(self.request.body.decode('utf-8'))
        except:
            data={"user":'None',"password":'None'}

        cookie = str(uuid4())

        #retornar True : cookie si se loguea
        #retornar False : 'null'
        response = {"cookie": None, "success": False}
        if registrar_cookie(data["user"], data["password"], cookie):
            self.set_secure_cookie("logged", cookie)
            response = {"cookie":cookie, "success": True}

        self.write(json.dumps(response))
