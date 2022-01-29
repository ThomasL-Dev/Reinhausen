import logging
import sys
import time

from flask import Flask as WebServer
from Bin.ApiServices import ApiServices
from Bin.RoutesServices import RoutesServices
from Bin.DataBaseServices import DataBaseServices
from Bin.Logging import Logging



class WebServices(object):

    def __init__(self):
        self._logging = Logging(position=self.__class__.__name__)

        self._app = None

        self.host = "0.0.0.0"
        self.port = 5002




    def start(self) -> None:
        print("#" * 15, 'Server Init', "#" * 15)
        self._app = WebServer(__name__)
        self.__disable_flask_log()
        self._logging.log("Server Starting")
        self.__on_start()
        self._app.run(host=self.host, port=self.port, debug=False)



    def __on_start(self):
        print("#" * 15, 'ROUTES', "#" * 15)
        route_s = RoutesServices(self._app)
        print("#" * 15, 'APIs', "#" * 15)
        api_s = ApiServices(self._app)
        print("#" * 15, 'DataBase', "#" * 15)
        db_s = DataBaseServices()
        db_s.create_db('accounts')
        if not db_s.check_if_table_exist("accounts", "erp"):
            db_s.create_table('accounts', "erp", ("id", "name", "pwd", "creationdate"))
            db_s.insert('accounts', 'erp', (0, "admin", "admin", "00:00:00 00/00/00"))


    def __disable_flask_log(self):
        # info, warning, etc
        self._app.logger.disabled = True
        log = logging.getLogger('werkzeug')
        log.disabled = True
        # cli
        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None


