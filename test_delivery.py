import unittest

from Delivery import calculate_delivery_cost


class CalculateDeliveryCostTest(unittest.TestCase):

    def test_minimal_valid_weight(self):
        cost, date = calculate_delivery_cost(0.1, 1, "обычный")
        self.assertEqual(cost, 205)
        self.assertEqual(date, "2026-09-04")


    def test_maximal_valid_weight(self):
        cost, date = calculate_delivery_cost(50.0, 5000, "опасный")
        self.assertEqual(cost, 38800)
        self.assertEqual(date, "2026-09-13")


    def test_invalid_weight_below_min(self):
        cost, date = calculate_delivery_cost(0.0, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")


    def test_invalid_weight_above_max(self):
        cost, date = calculate_delivery_cost(51.0, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")


    def test_invalid_distance_below_min(self):
        cost, date = calculate_delivery_cost(10.0, 0, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")


    def test_invalid_distance_above_max(self):
        cost, date = calculate_delivery_cost(10.0, 5001, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")


    def test_fragile_package(self):
        cost, date = calculate_delivery_cost(10.0, 1000, "хрупкий")
        self.assertEqual(cost, 6540)
        self.assertEqual(date, "2026-09-05")

    def test_dangerous_package(self):
        cost, date = calculate_delivery_cost(10.0, 1000, "опасный")
        self.assertEqual(cost, 7240)
        self.assertEqual(date, "2026-09-05")

    def test_express_delivery(self):
        cost, date = calculate_delivery_cost(10.0, 1000, "обычный", is_express=True)
        self.assertEqual(cost, 3120)
        self.assertEqual(date, "2026-09-04")

    def test_regular_package(self):
        cost, date = calculate_delivery_cost(10.0, 1000, "обычный")
        self.assertEqual(cost, 6240)
        self.assertEqual(date, "2026-09-05")


if __name__ == "__main__":
    unittest.main()
    