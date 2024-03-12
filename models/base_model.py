#!/usr/bin/python3
from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for k, v in kwargs.items():
            if k == '__class__':
                continue
            if '_at' in k:
                self.__dict__[k] = datetime.fromisoformat(v)
                continue
            self.__dict__[k] = v
        storage.new(self)

    def __str__(self):
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ndict = self.__dict__.copy()
        ndict['__class__'] = self.__class__.__name__
        ndict['created_at'] = self.created_at.isoformat()
        ndict['updated_at'] = self.updated_at.isoformat()
        return ndict
