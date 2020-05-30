import unittest
from config import TestingConfig
from app import db, create_app
from app.models import Store

class StoreTest(unittest.TestCase):
    """Store service RestAPI test cases"""

    def _init_db(self):
        """Seed db with test data"""
        store_1 = Store(name='flagship-SG',
                address='Woodlands',
                country='Singapore')
        store_2 = Store(name='J-Square',
                address='MacPherson',
                country='Singapore')
        store_3 = Store(name='Causeway Mall',
                address='Johore Bahru',
                country='Malaysia')
        db.session.bulk_save_objects([store_1, store_2, store_3])
        db.session.commit()

    def setUp(self):
        """Define test variables and initialize db"""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client

        with self.app.app_context():
            db.create_all()
            self._init_db()

    def test_api_get_store_list(self):
        """Test API get list of store (GET request)"""
        res = self.client().get('/store')
        self.assertEqual(res.status_code, 300)
        self.assertEqual(len(res.data), 3)

    def test_api_get_store_by_id(self):
        """Test API get single store by id (GET request)"""
        pass

    def test_api_create_new_store(self):
        """Test API create a store (POST request)"""
        pass

    def test_api_edit_store(self):
        """Test API modify an existing store (PUT request)"""
        pass

    def test_api_delete_store(self):
        """Test API remove an existing store (PUT request)"""
        pass

    def tearDown(self):
        """Clean up db session and variables"""
        with self.app.app_context():
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
