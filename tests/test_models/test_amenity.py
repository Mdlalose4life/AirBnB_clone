#!/usr/bin/python3
""" testing Amenity """
import unittest
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """ check BaseModel """
    def testpep8(self):
        """ testing codestyle """
        pepstylecode = models.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")
