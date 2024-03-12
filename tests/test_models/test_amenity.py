#!/usr/bin/python3

import os
import unittest

from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.objects = {}

    def test_name(self):
        myModel = Amenity()
        self.assertEqual(myModel.name, "")
