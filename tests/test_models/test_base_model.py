#!/usr/bin/python3
import os
import unittest
from datetime import datetime

from models.__init__ import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("gaga.json")
        except IOError:
            pass

        storage.objects = {}

    def test_id_generation(self):
        myModel = BaseModel()
        self.assertIsInstance(myModel.id, str)

    def test_created_at(self):
        myModel = BaseModel()
        self.assertIsInstance(myModel.created_at, datetime)

    def test_save_method(self):
        myModel = BaseModel()
        previous_updated_at = myModel.updated_at
        myModel.save()
        self.assertNotEqual(previous_updated_at, myModel.updated_at)

    def test_save_method_with_storage(self):
        myModel = BaseModel()
        myModel.name = "myModel"
        myModel.my_number = 89
        myModel.save()
        self.assertTrue(os.path.exists("gaga.json"))
        self.assertIn("BaseModel." + myModel.id, storage.all())

    def test_to_dict_method(self):
        myModel = BaseModel()
        obj_dict = myModel.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_str_method(self):
        myModel = BaseModel()
        expected_string = f"[BaseModel] ({myModel.id}) {myModel.__dict__}"
        self.assertEqual(str(myModel), expected_string)
