#!/usr/bin/python3

import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("gaga.json")
        except IOError:
            pass

        storage.objects = {}

    def test_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()

        storage.save()
        FileStorage._FileStorage__objects.clear()
        storage.reload()

        self.assertNotEqual(len(FileStorage._FileStorage__objects), 0)

    def test_storage_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)

        all_objs = storage.all()

        self.assertIn(obj1, all_objs.values())
        self.assertIn(obj2, all_objs.values())

    def test_check_type(self):
        file_path = FileStorage._FileStorage__file_path
        objects = FileStorage._FileStorage__objects

        self.assertIsInstance(file_path, str)
        self.assertIsInstance(objects, dict)

    def test_storage_new(self):
        obj1 = BaseModel()
        storage.new(obj1)

        self.assertIn(obj1, storage.all().values())

    def test_storage_save(self):
        obj1 = BaseModel()

        storage.new(obj1)
        storage.save()

        with open("gaga.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + obj1.id, text)
