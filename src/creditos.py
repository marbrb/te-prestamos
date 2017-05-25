from login import BaseHandler
from queries import obtener_cliente, obtener_creditos, crear_credito, actualizar_credito
import json

class CreditosHandler(BaseHandler):
    def get(self):
        """Listado creditos del usuario actual"""
        user = obtener_cliente(self.get_secure_cookie("logged"))
        if user:
            creditos = obtener_creditos(user)
            if creditos:
                self.write(json.dumps(creditos))
            else:
                #no hay creditos
                self.write("{}")
        else:
            self.write(json.dumps({"logged": False}))

    def post(self):
        """Crear un nuevo credito"""
        user = obtener_cliente(self.get_secure_cookie("logged"))
        if user:
            try:
                data = json.loads(self.request.body.decode('utf-8'))
            except Exception as e:
                self.write("Error al recivir el JSON.")
                return

            monto = data["monto"]
            interes = float(data["interes"])
            success = crear_credito(user, interes, monto)
            if success:
                self.write("Credito creado.")
            else:
                self.write("Error al crear el credito")
        else:
            self.write(json.dumps({"logged": False}))

    def put(self):
        user = obtener_cliente(1)
        if user:
            try:
                data = json.loads(self.request.body.decode('utf-8'))
            except Exception as e:
                self.write("Error al recivir el JSON.")
                return

            concepto_cliente = data["concepto_cliente"]
            id_credito = data["id_credito"]

            success = actualizar_credito(id_credito, concepto_cliente)
            if success:
                self.write("Credito actualizado.")
            else:
                self.write("Error al actualizar el credito")

        else:
            self.write(json.dumps({"logged": False}))
