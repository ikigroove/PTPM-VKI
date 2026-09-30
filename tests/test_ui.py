import unittest
from unittest.mock import patch
from src.console_user_interface import ConsoleUserInterface

class TestConsoleUserInterface(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '4', '5'])
    def test_get_triangle_sides(self, mock_input):
        ui = ConsoleUserInterface()

        result = ui.get_triangle_sides()

        self.assertEqual(result, (3, 4, 5))

if __name__ == "__main__":
    unittest.main()