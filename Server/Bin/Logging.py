import os
from datetime import datetime


class Logging(object):

    def __init__(self, position: str):
        self._position = position.replace("_", " ").upper()

        self.PATH_FOLDER_LOG = os.path.join(os.getcwd(), ".Logs")
        self.PATH_FOLDER_MONTHLY = os.path.join(self.PATH_FOLDER_LOG, datetime.now().strftime("%m-%Y"))
        self.PATH_FILE_LOG = os.path.join(self.PATH_FOLDER_MONTHLY, "{}.txt".format(position))



    def log(self, string: str) -> None:
        """"""
        log = "|{}|{}| | [{}] | [LOG]   | {} ".format(Logging.get_time(), Logging.get_date(), self._position, string)
        self.__write_in_log_file(log)
        print(log)

    def info(self, string: str) -> None:
        """"""
        log = "|{}|{}| | [{}] | [INFO]  | {} ".format(Logging.get_time(), Logging.get_date(), self._position, string)
        self.__write_in_log_file(log)
        print(log)

    def error(self, string: str) -> None:
        log = "|{}|{}| | [{}] | [ERROR] | {} ".format(Logging.get_time(), Logging.get_date(), self._position, string)
        self.__write_in_log_file(log)
        print(log)




    @classmethod
    def get_date(cls) -> str:
        return datetime.now().strftime("%d/%m/%Y")

    @classmethod
    def get_time(cls) -> str:
        return datetime.now().strftime("%H:%M:%S")



    def __write_in_log_file(self, log: str) -> None:
        self.__create_dirs()
        # write in log file
        with open(self.PATH_FILE_LOG, "a+") as log_file:
            log_file.write(log + "\n")
            log_file.close()

    def __create_dirs(self) -> None:
        self.__create_dir(self.PATH_FOLDER_LOG)
        self.__create_dir(self.PATH_FOLDER_MONTHLY)

    def __create_dir(self, path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)




