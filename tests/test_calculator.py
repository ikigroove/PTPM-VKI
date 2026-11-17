import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.calculator_page import CalculatorPage

class TestSimpleCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._options = Options()
        cls._options.add_argument("--headless=new")
        cls._options.add_argument("--window-size=1280,1024")
        cls._options.add_argument("--no-sandbox")
        cls._options.add_argument("--disable-dev-shm-usage")

    def setUp(self):
        self.driver = webdriver.Chrome(options=self._options)
        self.page = CalculatorPage(self.driver).open()

    def tearDown(self):
        self.driver.quit()

    def test_addition(self):
        self.assertEqual(self.page.calculate(2, 3, "+"), "5")

    def test_subtraction(self):
        self.assertEqual(self.page.calculate(10, 4, "-"), "6")

    def test_multiplication(self):
        self.assertEqual(self.page.calculate(6, 7, "*"), "42")

    def test_division(self):
        self.assertEqual(self.page.calculate(9, 3, "/"), "3")

if __name__ == "__main__":
    unittest.main()