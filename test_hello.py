import unittest
from hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello from Jenkins!")

if _name_ == "_main_":
    unittest.main()
