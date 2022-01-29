from ApiObject import *
from Bin.DataBaseServices import DataBaseServices


class db_table(ApiObject):


    def __init__(self):
        super(db_table, self).__init__()
        self.uri = "{}/<db_name>/table/<table_name>".format(self.uri.replace('/table', ''))



    def get(self, **url_params):
        return super(db_table, self).get()


    def on_get(self, **url_params):
        content = self.db_service.get_table_contents(url_params['db_name'], url_params['table_name'])
        return content