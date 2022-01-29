from ApiObject import *


class connect(ApiObject):


    def __init__(self):
        super(connect, self).__init__()
        self.uri = self.uri + "/<username>/<password>"


    def get(self, **url_params):
        return super(connect, self).get()


    def on_get(self, **url_params):
        content = self.db_service.get_content_where("accounts", "erp", "name", url_params['username'])
        id = content[0]
        name = content[1]
        pwd = content[2]
        creationdate = content[3]
        if name == url_params['username'] and pwd == url_params['password']:
            return "authorized"
        else:
            return "unauthorized"