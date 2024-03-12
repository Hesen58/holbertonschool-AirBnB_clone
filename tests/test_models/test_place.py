#!/usr/bin/python3

import os
import unittest

from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.objects = {}

    def test_city_id(self):
        myModel = Place()
        self.assertEqual(myModel.city_id, "")

    def test_user_id(self):
        myModel = Place()
        self.assertEqual(myModel.user_id, "")

    def test_name(self):
        myModel = Place()
        self.assertEqual(myModel.name, "")

    def test_description(self):
        myModel = Place()
        self.assertEqual(myModel.description, "")

    def test_number_rooms(self):
        myModel = Place()
        self.assertEqual(myModel.number_rooms, 0)

    def test_number_bathrooms(self):
        myModel = Place()
        self.assertEqual(myModel.number_bathrooms, 0)

    def test_max_guest(self):
        myModel = Place()
        self.assertEqual(myModel.max_guest, 0)

    def test_price_by_night(self):
        myModel = Place()
        self.assertEqual(myModel.price_by_night, 0)

    def test_latitude(self):
        myModel = Place()
        self.assertEqual(myModel.latitude, 0.0)

    def test_longitude(self):
        myModel = Place()
        self.assertEqual(myModel.longitude, 0.0)

    def test_amenity_ids(self):
        myModel = Place()
        self.assertEqual(myModel.amenity_ids, [])
