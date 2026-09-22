import unittest

from src.Delivery import calculate_delivery_cost


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

    def test_light_document_short_distance(self):
        cost, date = calculate_delivery_cost(0.5, 300, "обычный")
        self.assertEqual(cost, 1700)
        self.assertEqual(date, "2026-09-04")

    def test_heavy_parcel_long_distance(self):
        cost, date = calculate_delivery_cost(35.0, 4500, "обычный")
        self.assertEqual(cost, 34050)
        self.assertEqual(date, "2026-09-12")

    def test_medium_parcel_medium_distance(self):
        cost, date = calculate_delivery_cost(12.0, 2500, "обычный")
        self.assertEqual(cost, 15240)
        self.assertEqual(date, "2026-09-08")

    def test_dangerous_more_expensive_than_fragile(self):
        cost_fragile, _ = calculate_delivery_cost(10.0, 1000, "хрупкий")
        cost_dangerous, _ = calculate_delivery_cost(10.0, 1000, "опасный")
        self.assertEqual(cost_dangerous - cost_fragile, 700)

    def test_fragile_more_expensive_than_regular(self):
        cost_regular, _ = calculate_delivery_cost(10.0, 1000, "обычный")
        cost_fragile, _ = calculate_delivery_cost(10.0, 1000, "хрупкий")
        self.assertEqual(cost_fragile - cost_regular, 300)

    def test_heavy_costs_more_than_light_same_distance(self):
        cost_light, _ = calculate_delivery_cost(3.0, 1000, "обычный")
        cost_heavy, _ = calculate_delivery_cost(25.0, 1000, "обычный")
        self.assertGreater(cost_heavy, cost_light)

    def test_weight_coefficient_applied_correctly(self):
        cost, _ = calculate_delivery_cost(10.0, 100, "хрупкий")
        self.assertEqual(cost, 1140)

    def test_distance_affects_price_linearly(self):
        cost_short, _ = calculate_delivery_cost(1.0, 100, "обычный")
        cost_long, _ = calculate_delivery_cost(1.0, 600, "обычный")
        self.assertEqual(cost_long - cost_short, 2500)

    def test_distance_affects_delivery_date(self):
        _, date_short = calculate_delivery_cost(1.0, 500, "обычный")
        _, date_long = calculate_delivery_cost(1.0, 3000, "обычный")
        self.assertLess(date_short, date_long)

    def test_express_costs_less_than_regular_current_logic(self):
        cost_regular, _ = calculate_delivery_cost(10.0, 1000, "обычный")
        cost_express, _ = calculate_delivery_cost(10.0, 1000, "обычный", is_express=True)
        self.assertEqual(cost_regular, cost_express * 2)

    def test_express_delivers_faster(self):
        _, date_regular = calculate_delivery_cost(10.0, 2000, "обычный")
        _, date_express = calculate_delivery_cost(10.0, 2000, "обычный", is_express=True)
        self.assertLess(date_express, date_regular)

    def test_invalid_package_type(self):
        cost, date = calculate_delivery_cost(10.0, 1000, "скоропортящийся")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_all_invalid_returns_same_error(self):
        results = [
            calculate_delivery_cost(0.0, 100, "обычный"),      
            calculate_delivery_cost(10.0, 0, "обычный"),       
            calculate_delivery_cost(10.0, 100, "чужой тип"),   
        ]
        for cost, date in results:
            self.assertEqual(cost, -1)
            self.assertEqual(date, "0000-00-00")



if __name__ == "__main__":
    unittest.main()
    