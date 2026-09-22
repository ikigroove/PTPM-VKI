import unittest
from unittest.mock import MagicMock
from src.triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.logger = MagicMock()

    def test_equilateral(self):
        triangle = Triangle(3, 3, 3, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "равносторонний")

    def test_isosceles(self):
        triangle = Triangle(3, 3, 4, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "равнобедренный")

    def test_scalene(self):
        triangle = Triangle(3, 4, 5, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "разносторонний")

    def test_invalid_sides(self):
        triangle = Triangle(-1, 2, 3, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "не треугольник")

    def test_triangle_inequality(self):
        triangle = Triangle(1, 2, 10, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "не треугольник")

    def test_zero_sides(self):
        triangle = Triangle(0, 0, 0, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "не треугольник")

    def test_zero_one_side(self):
        triangle = Triangle(0, 3, 3, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "не треугольник")

    def test_one_negative_side(self):
        triangle = Triangle(3, -4, 5, self.logger)
        triangle.process()
        self.assertEqual(triangle.triangle_type, "не треугольник")

    def test_coordinates_not_computed_for_invalid(self):
        triangle = Triangle(-1, 2, 3, self.logger)
        triangle.process()
        self.assertEqual(triangle.coordinates, [(-1, -1), (-1, -1), (-1, -1)])

    def test_coordinates(self):
        triangle = Triangle(3, 4, 5, self.logger)
        triangle.process()
        
        expected_coordinates = [(0, 0), (5, 0), (3.2, 2.4)]
        
        for i in range(3):
            self.assertAlmostEqual(triangle.coordinates[i][0], expected_coordinates[i][0])
            self.assertAlmostEqual(triangle.coordinates[i][1], expected_coordinates[i][1])

    if __name__ == "__main__":
        unittest.main()