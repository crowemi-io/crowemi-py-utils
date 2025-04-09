import os
import unittest
from crowemi.cloud.gcp.auth import get_gcp_id_token
import requests


class TestGcp(unittest.TestCase):

    def setUp(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
        path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        return super().setUp()

    def test_get_default_credential_token(self):
        token = get_gcp_id_token("")
        self.assertIsInstance(token, str)
        self.assertTrue(token != "")