#!/usr/bin/python3

import os
import unittest

from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.objects = {}

    def test_place_id(self):
        myModel = Review()
        self.assertEqual(myModel.place_id, "")

    def test_user_id(self):
        myModel = Review()
        self.assertEqual(myModel.user_id, "")

    def test_text(self):
        myModel = Review()
        self.assertEqual(myModel.text, "")
