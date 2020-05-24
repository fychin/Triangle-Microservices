import unittest
import os

class StoreTest(unittest.TestCase):
    """Store service RestAPI test cases"""

    def setUp(self):
        """Define test variables and initialize db"""
        pass

    def test_api_get_store_list(self):
        """Test API get list of store (GET request)"""
        pass
    
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
        pass


if __name__ == '__main__':
    unittest.main()
