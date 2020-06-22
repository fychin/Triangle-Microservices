import unittest
from app import db
from app.models import Store
from app.store import app


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
        self.existing_stores_list = [store_1, store_2, store_3]
        db.session.bulk_save_objects(self.existing_stores_list)
        db.session.commit()

    def setUp(self):
        """Define test variables and initialize db"""
        self.app = app
        self.client = self.app.test_client

        with self.app.app_context():
            db.create_all()
            self._init_db()

    def test_api_health_check(self):
        """Test service health-check (GET request)"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertDictEqual(data, {"service": "Store", "status": "healthy"})

    def test_api_get_store_list(self):
        """Test API get list of store (GET request)"""
        res = self.client().get('store')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data), 3)

    def test_api_get_store_by_id(self):
        """Test API get single store by id (GET request)"""
        res = self.client().get('store/2')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content_type, 'application/json')
        data = res.get_json()
        self.assertDictEqual({
            'id': 2,
            'name': 'J-Square',
            'address': 'MacPherson',
            'country': 'Singapore'
        }, data)

    def test_api_create_new_store(self):
        """Test API create a store (POST request)"""
        res = self.client().post('store', json={
            'name': 'New-Store',
            'address': '5-11 Madison Ave',
            'country': 'United States'
        })
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertDictEqual({
            'id': 4,
            'name': 'New-Store',
            'address': '5-11 Madison Ave',
            'country': 'United States'
        }, data)

    def test_api_edit_store(self):
        """Test API modify an existing store (PUT request)"""
        res = self.client().put('store/4', json={
            'name': 'California Flagship',
            'address': '3 Genesee Ave, La Jolla, San Diego',
            'country': 'United States'
        })
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertDictEqual({
            'id': 4,
            'name': 'California Flagship',
            'address': '3 Genesee Ave, La Jolla, San Diego',
            'country': 'United States'
        }, data)

    def test_api_delete_store(self):
        """Test API remove an existing store (PUT request)"""
        res = self.client().delete('store/3')
        self.assertEqual(res.status_code, 204)

    def tearDown(self):
        """Clean up db session and variables"""
        with self.app.app_context():
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
