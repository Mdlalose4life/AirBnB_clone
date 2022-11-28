#!/usr/bin/python3
"""Testing Place"""
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """Function that checks Basemodel"""
    def testpep8(self):
        """CodeStyling"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0, 
                        "Found code style errors (and warnings).")
