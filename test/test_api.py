import unittest
import requests
import json

class TestItemEndpoint(unittest.TestCase):
    base_url = "http://localhost:8080/items/"

    def test_create_items(self):
        data = {"name": "item1"}
        response = requests.post(self.base_url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)

        data = {"name": "item2"}
        response = requests.post(self.base_url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)

    def test_get_items(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        response = requests.delete(self.base_url + "item1")
        self.assertEqual(response.status_code, 200)

        response = requests.delete(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_items_after_deletion(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)  # Assuming only one item left after deletion

if __name__ == '__main__':
    unittest.main()
