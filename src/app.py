from uuid import uuid4
from tornado.ioloop import IOLoop
from login import LoginHandler, BaseHandler
from creditos import CreditosHandler
from pagos import PagosHandler, PagoHandler
from tornado import web
import os


class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html")

class Application:
    def __init__(self):
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "login_url": "/login",
            "xsrf_cookies": True,
        }

        self.app = web.Application([
                    web.url(r"/$", MainHandler),
                    web.url(r"/creditos", CreditosHandler),

                    web.url(r"/pagos/([0-9]+)", PagosHandler),

                    web.url(r"/pago/([0-9]+)", PagoHandler),

                    #quejeso
                    web.url(r"/login", LoginHandler),
                    (r"/static/(.*)", web.StaticFileHandler, {"path": "../static",
                                                              "default_filename": "index.html"},),
        ], cookie_secret=str(uuid4()), deafult_host='localhost')

    def run(self):
        self.app.settings["template_path"] = "../"
        self.app.listen(8888)
        IOLoop.current().start()


if __name__ == '__main__':
    try:
        applicaction = Application()
        applicaction.run()
    except KeyboardInterrupt:
        print("Server Stoped.")
        exit(0)
