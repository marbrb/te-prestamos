from login import BaseHandler
from queries import obtener_cliente, obtener_pagos, actualizar_pago
import json

class PagosHandler(BaseHandler):
    def get(self, id_credito):
        """Listado pagos del credito"""
        user = obtener_cliente(self.get_secure_cookie("logged"))
        if user:
            pagos = obtener_pagos(id_credito)
            if pagos:
                self.write(json.dumps(pagos))
            else:
                self.write("{}")
        else:
            self.write(json.dumps({"logged": False}))

class PagoHandler(BaseHandler):
    def put(self, id_pago):
        """actualizar pago"""
        user = obtener_cliente(self.get_secure_cookie("logged"))
        if user:
            estado = self.get_argument("estado")
            success = actualizar_pago(id_pago, estado)
            if success:
                self.write("Pago actualizado.")
            else:
                self.write("Error al actualizar el pago, estado incorrecto.")
        else:
            self.write(json.dumps({"logged": False}))
