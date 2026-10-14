import unittest
from converter import Converter

class TestConverter(unittest.TestCase):
    def test_positive_range(self):
        self.assertEqual(Converter.do(50.0), 50)
        self.assertEqual(Converter.do(100.6), 100)
        self.assertEqual(Converter.do(100.7), 1000)
        self.assertEqual(Converter.do(150.0), 1000)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    def test_negative_range(self):
        self.assertEqual(Converter.do(-10.0), -15)
        self.assertEqual(Converter.do(-30.4), -35)
        self.assertEqual(Converter.do(-30.5), -2000)
        self.assertEqual(Converter.do(-50.0), -2000)

    def test_boundary_values(self):
        self.assertEqual(Converter.do(-30.4), -35)
        self.assertEqual(Converter.do(-30.5), -2000)
        self.assertEqual(Converter.do(100.7), 1000)
        self.assertEqual(Converter.do(100.6), 100)

    def test_invalid_precision(self):
        with self.assertRaises(ValueError):
            Converter.do(10.123)
        with self.assertRaises(ValueError):
            Converter.do(-10.123)



# x ∈ [100.7; + ∞) -> метод возвращает число 1000.
# x ∈ (0; 100.7) -> метод возвращает целую часть числа x путем отбрасывания дробной части (эквивалентно int(x)).
# x == 0.0 -> генерируется исключение ValueError (аналог ArgumentException).
# x ∈ [-30.4; 0) -> метод возвращает целую часть числа x путем отбрасывания дробной части (эквивалентно int(x)) минус 5.
# x ∈ (-∞ ; -30.5] -> метод возвращает число -2000.