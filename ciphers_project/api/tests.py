from django.test import TestCase
from .cipher import encoder

# Create your tests here.
# test for cipher.py
class CipherTest(TestCase):
    def test_decoder(self):
        self.assertEqual(encoder("abc", 1), "bcd")
        self.assertEqual(encoder("hello", 3), "khoor")
        self.assertEqual(encoder("hello", 0), "hello")
        