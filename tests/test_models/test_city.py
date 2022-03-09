#!/usr/bin/python3
"""
has the test_city classes
 """

from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8
import unittest
import inspect
from datetime import datetime

class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")
    
    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class test_City(unittest.TestCase):
    """
    tests city class
    """

    def test_subclass(self):
        """
        tests city is a subclass of basemodel
         """
        city = City()
        self.assertIsInstance(City, BaseModel)
        self.assertTrue(hasattr(city, "id")
        self.assertTrue(hasattr(city, "created_at")
        self.assertTrue(hasattr(city, "updated_at)

    def test_state_id(self):
        """
        tests that the city has a state attribute
        """
        city = city()
        self.assertEqual(hasattr(city, "state_id"))
        if models.storage_t == 'db':
          self.assertEqual(city.state_id, None)
        else
          self.assertEqual(city.state_id, "")

    def test_name(self):
        """
        tests that a city has an attribute name
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        if models.storage_t == 'db':
          self.assertEqual(city.name, None)
        else
          self.assertEqual(city.name, "")
