import unittest
import calculator as calc

class TestCalc (unittest.TestCase):
  def test_add (self):
    self.assertEqual(calc.add(43, 25), 68)
    self.assertEqual(calc.add(-1, 1), 0)
    self.assertEqual(calc.add(-1, -1), -2)

  def test_subtract (self):
    self.assertEqual(calc.subtract(43, 25), 18)
    self.assertEqual(calc.subtract(-1, 1), -2)
    self.assertEqual(calc.subtract(-1, -1), 0)

  def test_multiply (self):
    self.assertEqual(calc.multiply(43, 25), 1075)
    self.assertEqual(calc.multiply(-1, 1), -1)
    self.assertEqual(calc.multiply(-1, -1), 1)
    
  def test_divide (self):
    self.assertEqual(calc.divide(10, 2), 5)
    self.assertEqual(calc.divide(43, 25), 1.72)
    self.assertEqual(calc.divide(-1, 1), -1)
    self.assertEqual(calc.divide(-1, -1), 1)
    self.assertEqual(calc.divide(2, 0), False)

  def test_numeric (self):
    self.assertFalse(calc.check_is_numeric('-10'))
    self.assertTrue(calc.check_is_numeric('10'))
    self.assertFalse(calc.check_is_numeric('abc'))
    self.assertFalse(calc.check_is_numeric('10abc'))
    self.assertFalse(calc.check_is_numeric('abc10'))
    self.assertFalse(calc.check_is_numeric('abc10asd'))

if __name__ == '__main__':
  unittest.main()