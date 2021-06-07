import calculator
import unittest

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 2), 4)
    def test_sub(self):
        self.assertEqual(calculator.sub(7, 4), 3)
    def test_mul(self):
        self.assertEqual(calculator.mul(8, 3), 24)
    def test_div(self):
        self.assertEqual(calculator.div(24, 8), 3)

if __name__ == '__main__':
    unittest.main()
