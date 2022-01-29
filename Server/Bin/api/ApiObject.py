from flask_restful import Resource as Resource
from flask import redirect
import flask
from Bin.DataBaseServices import DataBaseServices
from Bin.Logging import Logging
from Bin.Utils import get_localisation


class ApiObject(Resource):


    def __init__(self):
        self._logging = Logging(position="API({})".format(self.__class__.__name__))
        self.MSG_ROUTE_ON_CONN = "'{} | {}' Accessing to Web Api '{} - {}'"
        self.name = self.__class__.__name__
        self.uri = "/api/{}".format(str(self.__class__.__name__).replace("_", "/"))
        self.full_url: str or None = None
        self.db_service = DataBaseServices()



    def __repr__(self):
        return (f'API('
                f'name={self.name!r}, '
                f'uri={self.uri!r}'
                f')')



    def init_request(self) -> dict:
        """ :return """
        remote_addr = flask.request.remote_addr
        loc = get_localisation(remote_addr)
        requested_method = flask.request.method
        self.full_url = str(flask.request.path)
        self._logging.info(self.MSG_ROUTE_ON_CONN.format(remote_addr, loc.replace(" ", " | "), requested_method, self.uri))
        return {
            'method': requested_method,
            'uri': self.full_url,
            'ip': remote_addr,
            'loc': loc,
                }



    def get(self, **args):

        return redirect("/", code=302)
        """try:
            init = self.init_request()
        except Exception as e:
            init = "On Init 'GET' : {}".format(e)

        try:
            reponse = self.on_get(**args)
        except Exception as e:
            reponse = "On Reponse 'GET' : {}".format(e)

        return {
            'request': init,
            'reponse': reponse,
        }"""


    def post(self, **args):
        try:
            init = self.init_request()
        except Exception as e:
            init = "On Init 'POST' : {}".format(e)

        try:
            reponse = self.on_get(**args)
        except Exception as e:
            reponse = "On Reponse 'POST' : {}".format(e)

        return {
            'request': init,
            'reponse': reponse,
        }



    def on_get(self, **args) -> dict:
        """ on get actions """
        return {}

    def on_post(self, **args) -> dict:
        """ on get actions """
        return {}




    def get_last_param(self):
        if self.full_url is not None:
            return self.full_url.split('/')[-1]