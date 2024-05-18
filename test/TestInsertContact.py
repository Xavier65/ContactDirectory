import unittest
import os
from dotenv import load_dotenv

from manager.DataManager import DataManager


class TestInsertContact(unittest.TestCase):
    def test_validate_enviroment(self):
        load_dotenv()
        self.DATABASE = os.getenv("DATABASE")
        self.assertNotEqual(self.DATABASE, None)

    def test_database_created(self):
        self.manager = DataManager(self.DATABASE)
        self.assertEqual(len(self.manager.validate()), 4)


unittest.main()
