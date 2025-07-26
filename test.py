# test.py

import unittest
import json
from app import app  # This imports the Flask app from app.py

class ChatbotFlaskTest(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_greeting(self):
        response = self.app.post('/chat', 
                                 data=json.dumps({'message': 'Hello'}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', data)
        self.assertTrue('hello' in data['response'].lower() or 'hi' in data['response'].lower())

    def test_farewell(self):
        response = self.app.post('/chat',
                                 data=json.dumps({'message': 'Bye'}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', data)
        self.assertTrue('bye' in data['response'].lower() or 'goodbye' in data['response'].lower())

    def test_unknown_input(self):
        response = self.app.post('/chat',
                                 data=json.dumps({'message': 'xyzabc'}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', data)
        self.assertTrue('don\'t understand' in data['response'].lower() or 'sorry' in data['response'].lower())

if __name__ == '__main__':
    unittest.main()
