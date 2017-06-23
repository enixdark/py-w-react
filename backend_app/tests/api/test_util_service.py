import os
import unittest
# from faker import Faker
from app import application
import json


class TestApi(unittest.TestCase):

    def setUp(self):
        # self.db, application.config['DATABASE'] = tempfile.mkstemp()
        # application.config.from_pyfile('config/development.cfg')
        application.config['TESTING'] = True
        self.client = application.test_client()
        self.text = "Google is a search engine service, google is also an engine for a lot of other services and tools"

    def tearDown(self):
        pass

    def test_match_text(self):
        
        response = self.client.get(
            '/parse?text=%s&subtext=%s' % (self.text,"google")
        )
        data = json.loads(response.data)
        self.assertEqual(data, "1, 36")

    def test_invalid_query(self):
        response = self.client.get(
            '/parse?hello=%s&world=%s' % (self.text,"")
        )
        data = json.loads(response.data)
        self.assertEqual(data, None)

if __name__ == '__main__':
    unittest.main()
