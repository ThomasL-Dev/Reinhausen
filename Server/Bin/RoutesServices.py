from Bin.Logging import Logging
from Bin.Utils import get_localisation
from Bin.ApiServices import ApiServices
from flask import *


class RoutesServices(object):


    _ROUTES = {'/': {"name": "index", "uri": "/"},}


    def __init__(self, webservice=None):
        self._logging = Logging(position=self.__class__.__name__)
        self._MSG_ROUTE_ON_CONN = "'{} | {}' Accessing to Web Page '{} - {}'"

        self._webapp = webservice
        # self.__load_routes__()



    def index(self):
        return render_template("index.html",
                               init_page=self.__init_header_page__(),
                               routes=self._ROUTES,
                               apis=self.__api_list__(),
                               )



    def __init_header_page__(self) -> dict:
        """ :return remote_addr """
        remote_addr = request.remote_addr
        loc = get_localisation(remote_addr)
        requested_method = request.method
        self._logging.info(self._MSG_ROUTE_ON_CONN.format(remote_addr, loc.replace(" ", " | "), requested_method, self._ROUTES['/']['uri']))
        return {
            'method': requested_method,
            'uri': self._ROUTES['/']['uri'],
            'ip': remote_addr,
            'loc': loc,
                }

    def __load_routes__(self) -> None:
        self._logging.log("Loading Routes ...")
        for r in self._ROUTES:
            self._webapp.add_url_rule(self._ROUTES[r]['uri'], self._ROUTES[r]['name'], getattr(self, self._ROUTES[r]['name']))
            self._logging.log("Adding Route '{}' with uri '{}'".format(self._ROUTES[r]['name'], self._ROUTES[r]['uri']))
        self._logging.log("Routes Loaded")

    def __api_list__(self) -> dict:
        return ApiServices().get_api_uri_list()












