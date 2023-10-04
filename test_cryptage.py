import unittest

class TestCrypt(unittest.TestCase):

    def test_crypt_simple(self):
        self.assertEqual(crypt("abc"), "bcd")

    def test_crypt_mixed_case(self):
        self.assertEqual(crypt("Hello, World!"), "Ifmmp- Xpsme!")

if __name__ == '__main__':
    unittest.main()


