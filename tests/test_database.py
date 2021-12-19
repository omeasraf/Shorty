import random
import string
import unittest
import os.path

from database import Database


class DatabaseTest(unittest.TestCase):

    def test_database_exists(self):
        db = Database("tests.db")
        db.createDB()
        exists = os.path.exists("tests.db")
        self.assertTrue(exists)
    
    def test_id(self):
        db = Database("tests.db")
        db.createDB()

        LETTERS = string.ascii_lowercase + string.digits
        id = "".join(random.choice(LETTERS) for i in range(10))

        db.create("https://omeasraf.com", id)

        self.assertEqual(db.find("https://omeasraf.com").id, id)


if __name__ == "__main__":
    unittest.main()