import inspect
import os
import sys


class ModuleLoader(object):

    def __init__(self, dir_path: str=None):
        """  """
        if dir_path is not None:
            self._LOADED_MODULE = []
            self._dir_path = self.__fix_folder_path_if_needed(dir_path)
            self._load_modules_in_folder()



    def get_module_list(self) -> list:
        return self._LOADED_MODULE

    def get_module_by_name(self, classname: str):
        for _class in self._LOADED_MODULE:
            if classname in str(_class):
                return _class
        return None



    def _load_modules_in_folder(self):
        """ Load Api in folder given """
        # itterate (folder path, folder name, files) in folder and sub folder
        for (dir_path, dirnames, filenames) in os.walk(self._dir_path):
            # ittterate foute file in folder
            for _filename in self.__find_module_file_in_folder(dir_path):
                # load route class in file
                _class = self.__load_module_in_file(_filename)
                # if route class is not None
                if _class is not None:
                    self._LOADED_MODULE.append(_class)


    def __find_module_file_in_folder(self, dir_path: str):
        # Add path to the system path
        self.__add_dirpath_to_syspath(dir_path)
        # Load all the files in path
        for _file in os.listdir(dir_path):
            # Ignore anything that isn't a .py file and file name start by "Skill"
            if len(_file) > 3 and _file[-3:] == '.py':
                # get skill file name without extension
                _filename = _file[:-3]
                yield _filename

    def __load_module_in_file(self, filename: str):
        try:
            # format the class in file (ClassName.ClassName)
            formatted_class = self.__create_module_name(filename)
            # get Class Module and ClassName
            route_class, module_class_name, class_name = self.__get_module_infos(formatted_class)
            # Import the module
            __import__(module_class_name, globals(), locals(), ['*'])
            # Get the class
            _class = getattr(sys.modules[module_class_name], class_name)
            # Check if its a class
            if inspect.isclass(_class):
                # Return class
                return _class
            else:
                return None
        except Exception as e:
            print("[{}] {}".format(self.__class__.__name__, e))
            pass

    def __get_module_infos(self, route_file_name: str):
        splitted_class_name = route_file_name.split('.')
        module_class_name = '.'.join(splitted_class_name[:-1])
        class_name = splitted_class_name[-1]
        return splitted_class_name, module_class_name, class_name

    def __create_module_name(self, skill_file_name: str):
        # format skill class
        if "." not in skill_file_name:
            return skill_file_name + "." + skill_file_name
        else:
            return skill_file_name


    def __fix_folder_path_if_needed(self, path: str):
        # if not start with "/"
        if path[-1:] != '/':
            path += '/'
        return path

    def __add_dirpath_to_syspath(self, dir_path: str):
        """ Add path to the system path """
        sys.path.append(dir_path)






