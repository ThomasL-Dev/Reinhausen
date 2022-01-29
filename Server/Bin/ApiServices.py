import os
from flask_restful import Api as WebApi
from Bin.ModuleLoader import ModuleLoader as ApiLoader
from Bin.Logging import Logging




class ApiServices(object):

    _API_LIST = None

    def __init__(self, webservices=None):
        self._logging = Logging(position=self.__class__.__name__)
        self.PATH_FILES_API = os.path.join(__file__.replace(self.__class__.__name__ + ".py", ""), 'api')

        if webservices is not None:
            # init API in Web Service
            self._web_api = WebApi(webservices)
            # load Api
            self.load_api()


    def get_api_uri_list(self) -> dict:
        apis = {}
        for api in ApiLoader(dir_path=self.PATH_FILES_API).get_module_list():
            name = api().name
            uri = api().uri
            if "Object" not in uri:
                if "<" not in uri and ">" not in uri:
                    apis[name] = {
                        'name': name,
                        'uri': uri,
                    }
        return apis


    def load_api(self):
        self._logging.log("Loading APIs ...")
        api_loader = ApiLoader(dir_path=self.PATH_FILES_API)
        self._API_LIST = api_loader.get_module_list()
        for _api in self._API_LIST:
            api = _api
            uri = _api().uri
            if "Object" not in uri:
                self.__add_api(api, uri)
                self._logging.log("Adding API '{}' with uri '{}'".format(api.__name__, uri))
            del api, uri
        self._logging.log("APIs Loaded")



    def __add_api(self, clss: classmethod, web_uri: str) -> None:
        """ add web_uri: str"""
        self._web_api.add_resource(clss, web_uri)

