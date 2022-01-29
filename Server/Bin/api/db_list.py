from ApiObject import *
from Bin.DataBaseServices import DataBaseServices


class db_list(ApiObject):


    def __init__(self):
        super(db_list, self).__init__()
        self.uri = self.uri



    def on_get(self):
        list_db = self.db_service.get_db_list()
        db = {}
        for _db in list_db:
            db["DataBases"] = _db
        return db