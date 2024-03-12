#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = 'gaga.json'
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        objs = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(objs))

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for k, v in objs.items():
                    clsnm = k.split(".")[0]
                    self.__objects[k] = eval(clsnm)(**v)
        except FileNotFoundError as _:
            pass
