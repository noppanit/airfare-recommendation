from tests.helpers.config_parser import get_config
from airfare.atc import delete_all  

import unittest

class GraphTestContext(unittest.TestCase):

    def setUp(self):
        delete_all()
        
    def tearDown(self):
        delete_all()
