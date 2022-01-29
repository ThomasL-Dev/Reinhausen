from ApiObject import *



class db(ApiObject):


    def __init__(self):
        super(db, self).__init__()
        self.uri = self.uri + "/<db_name>"


    def get(self, **url_params):
        return super(db, self).get()


    def on_get(self, **url_params):
        return {
            'db': url_params['db_name'],
            'tables': self.db_service.get_all_tables(url_params['db_name'])
        }

