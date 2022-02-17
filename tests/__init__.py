import unittest

def my_test_suite():
    test_loader = unittest.TestLoader()
    return test_loader.discover('.', pattern='*_test.py')