import main
import unittest

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        param = 20
        result = main.do_stuff(param)
        self.assertEqual(result, 25)

    def test_do_stuff2(self):
        param = 'rfrfr'
        result = main.do_stuff(param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        param = None
        result = main.do_stuff(param)
        self.assertEqual(result, 'Please enter valid num')

if __name__ == '__main__':
    unittest.main()
