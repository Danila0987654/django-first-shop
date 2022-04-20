import unittest

def suite():
    return unittest.TestLoader().discover("store.tests", pattern="*.py")
