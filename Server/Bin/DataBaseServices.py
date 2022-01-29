import os
import sqlite3
import time

from Bin.Logging import Logging
from Bin.Utils import create_dir



class DataBaseServices(object):

    def __init__(self):
        """  """
        self.PATH_FOLDER_DB = os.path.join(__file__.replace(self.__class__.__name__ + ".py", ""), 'db')
        self._logging = Logging(position="DataBaseService")



    def insert(self, dbname: str, tablename: str, values: tuple=None):
        self._logging.info("INSERTING Values '{}' in Table '{}' from Database '{}'".format(values, tablename, dbname))
        if len(values) == len(self.get_columns_name_from_table(dbname, tablename)):
            try:
                db_conn, cursor = self.connect_db(dbname)
                # generate a new insert request with table name
                column = str(tuple(self.get_columns_name_from_table(dbname, tablename)))
                req = "INSERT INTO {} {} VALUES {}".format(tablename, column, values)
                self.__execute(db_conn, cursor, req, commit=True)
                self.__close(db_conn, cursor)
                self._logging.info("INSERTING finished".format(values, tablename, dbname))
            except Exception as e:
                self._logging.error("INSERTING ERROR : {}".format(values, tablename, dbname, e))
        else:
            self._logging.error("INSERTING ERROR of Values '{}' in Table '{}' from Database '{}' failed : not enough values".format(values, tablename, dbname))

    def remove(self, dbname: str, tablename: str, where=None, where_value=None):
        self._logging.info("REMOVING Values '{}' where '{}' in Table '{}'".format(tablename, where, where_value))
        # execute remove request where "value" is "value"
        db_conn, cursor = self.connect_db(dbname)
        req = "DELETE from {} where {} = '{}'"
        self.__execute(db_conn, cursor, req.format(tablename, where, where_value))
        self.__close(db_conn, cursor)
        self._logging.info("REMOVING Values '{}' where '{}' in Table '{}' finished".format(tablename, where, where_value))


    def get_all_tables(self, dbname: str):
        # init tables list
        out = []
        db_conn, cursor = self.connect_db(dbname)
        # execute select table request
        req = '''SELECT name FROM sqlite_master WHERE type='table';'''
        # get everyuthing
        tables = self.__execute(db_conn ,cursor, req, fetch=True)
        if tables:
            # itterate tables
            for table in tables:
                try:
                    # add table name to list
                    out.append(table[0])
                except:
                    continue
            self.__close(db_conn, cursor)
            # return table list
            return out

    def get_db_list(self):
        return [db.split(".")[0] for db in os.listdir(self.PATH_FOLDER_DB) if db.split(".")[1] == "db"]

    def get_table_contents(self, dbname: str, tablename: str, by: str='id'):
        try:
            db_conn, cursor = self.connect_db(dbname)
            req = "SELECT * FROM {}".format(tablename)
            content = self.__execute(db_conn, cursor, req, fetch=True)
            return content
        except Exception as e:
            self._logging.error(str(e))
            return str(e)


    def get_content_where(self, dbname: str, tablename: str, where: str, where_value: str):
        try:
            db_conn, cursor = self.connect_db(dbname)
            req = 'SELECT * FROM {} WHERE {} = "{}"'.format(tablename, where, where_value)
            content = self.__execute(db_conn, cursor, req, fetch=True)
            return content[0]
        except Exception as e:
            self._logging.error(str(e))
            return str(e)


    def get_columns_name_from_table(self, dbname: str, table_name: str):
        db_conn, cursor = self.connect_db(dbname)
        # select every tables
        req = "select * from {}".format(table_name)
        cursor.execute(req)
        # list every table names
        names = list(map(lambda x: x[0], cursor.description))
        self.__close(db_conn, cursor)
        # return tables name
        return names

    def create_db(self, name: str):
        _n = "{}.db".format(os.path.join(self.PATH_FOLDER_DB, name))
        if not os.path.exists(_n):
            self._logging.info("CREATING Database '{}'".format(name))
            with open(_n, "w+") as db:
                db.close()
        else:
            self._logging.info("Database '{}' already exist".format(name))

    def create_table(self, dbname: str, tablename: str, column: tuple):
        self._logging.info("CREATING Table '{}' in Database '{}'".format(tablename, dbname))
        try:
            db_conn, cursor = self.connect_db(dbname)
            req = "CREATE TABLE {} {}".format(tablename, column)
            self.__execute(db_conn, cursor, req)
            self._logging.info("CREATING Table '{}' in Database '{}' finished".format(tablename, dbname))
            self.__close(db_conn, cursor)
        except Exception as e:
            self._logging.error("ERROR CREATING Table '{}' : {}".format(tablename, e))


    def connect_db(self, name: str) -> sqlite3.connect:
        try:
            create_dir(self.PATH_FOLDER_DB)

            if os.path.exists('{}.db'.format(os.path.join(self.PATH_FOLDER_DB, name))):

                db_conn = sqlite3.connect('{}.db'.format(os.path.join(self.PATH_FOLDER_DB, name)))
                cursor = db_conn.cursor()

                return db_conn, cursor

            self._logging.info("ERROR Couldn't Find to Database '{}'".format(name))
            return None, None
        except Exception as e:
            self._logging.info("ERROR Couldn't Connect to Database '{}' : {}".format(name, e))
            return None, None

    def check_if_table_exist(self, dbname: str, table: str):
        tables = self.get_all_tables(dbname)
        if tables is not None:
            for _table in tables:
                if table in _table:
                    return True
        return False



    def __execute(self, db_conn=None, cursor=None, string: str=None, values: dict=None, fetch: bool=False, commit: bool=True):
        if cursor is not None and string is not None:
            time.sleep(0.5)
            try:
                if values is None:
                    cursor.execute(string)
                    self._logging.info("EXECUTING request '{}'".format(string))
                else:
                    cursor.execute(string, values)
                    self._logging.info("EXECUTING request '{}' values '{}'".format(string, values))

                if commit:
                    db_conn.commit()

                if fetch:
                    return cursor.fetchall()
                return False
            except Exception as e:
                if values is None:
                    self._logging.error("ERROR Couldn't Execute request '{}' : {}".format(string, e))
                else:
                    self._logging.error("ERROR Couldn't Execute request '{}' values '{}' : {}".format(string, values, e))
                raise e

    def __close(self, db_conn, cursor):
        cursor.close()
        db_conn.close()

