import unittest
from crowemi_cloud.gcp import get_default_credential_token
import requests


class TestGcp(unittest.TestCase):

    def test_get_default_credential_token(self):
        token = get_default_credential_token()
        self.assertIsInstance(token, str)
        self.assertTrue(token != "")