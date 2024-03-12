#!/usr/bin/python3

import os
import unittest

from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.objects = {}

    def test_check_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        myModel = User()
        myModel.email = "mymail@gmail.com"
        self.assertEqual(myModel.email, "mymail@gmail.com")

    def test_password(self):
        myModel = User()
        myModel.password = "Baku"
        self.assertEqual(myModel.password, "Baku")

    def test_first_name(self):
        myModel = User()
        myModel.first_name = "Ganja"
        self.assertEqual(myModel.first_name, "Ganja")

    def test_last_name(self):
        myModel = User()
        myModel.last_name = "Shaki"
        self.assertEqual(myModel.last_name, "Shaki")
