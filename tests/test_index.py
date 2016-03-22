import os
import unittest
from src.app import app


class YouStatAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        # Fix to make 'make_response' work.
        os.chdir('../src/')
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_page_loading(self):
        rv = self.app.get('/')
        assert 'YouStat Analyzer' in rv.data
