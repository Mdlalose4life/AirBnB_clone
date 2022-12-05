#!/usr/bin/python3
""" testing Amenity """
import unittest 
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel

class Amenity_testing(unittest.TestCase):
    """ check BaseModel """
    def module_doc(self):
        """Module Documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")
