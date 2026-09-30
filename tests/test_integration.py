import unittest
from unittest.mock import MagicMock, patch

from src.controller import Controller
from src.console_user_interface import ConsoleUserInterface


class TestControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.db_patcher = patch("src.controller.Database")
        self.mock_db_class = self.db_patcher.start()    
        self.mock_db_instance = MagicMock()
        self.mock_db_class.return_value = self.mock_db_instance

        self.notify_patcher = patch("src.controller.EmailNotificationService")
        self.mock_notify_class = self.notify_patcher.start()
        self.mock_notify_instance = MagicMock()
        self.mock_notify_class.return_value = self.mock_notify_instance

        self.ui = MagicMock(spec=ConsoleUserInterface)
        self.controller = Controller(self.ui)

    def tearDown(self):
        self.db_patcher.stop()
        self.notify_patcher.stop()

    def test_database_insert_when_cache_miss(self):
        self.ui.get_triangle_sides.return_value = (3.0, 4.0, 5.0)
        self.mock_db_instance.find_triangle.return_value = None

        self.controller.run()

        self.mock_db_instance.find_triangle.assert_called_once_with(3.0, 4.0, 5.0)

        self.mock_db_instance.insert_triangle.assert_called_once_with(
            3.0, 4.0, 5.0, "разносторонний", ""
        )

    def test_database_cache_hit_does_not_insert(self):
        self.ui.get_triangle_sides.return_value = (5.0, 5.0, 5.0)
        self.mock_db_instance.find_triangle.return_value = ("равносторонний", "")

        self.controller.run()

        self.mock_db_instance.find_triangle.assert_called_once_with(5.0, 5.0, 5.0)
        self.mock_db_instance.insert_triangle.assert_not_called()

    def test_notification_service_receives_two_messages(self):
        self.ui.get_triangle_sides.return_value = (3.0, 4.0, 5.0)
        self.mock_db_instance.find_triangle.return_value = None

        self.controller.run()

        self.assertEqual(self.mock_notify_instance.notify.call_count, 2)

        notify_calls = [
            call.args[0] for call in self.mock_notify_instance.notify.call_args_list
        ]
        self.assertIn("Тип треугольника: разносторонний", notify_calls)
        self.assertIn("Сообщение об ошибке: ", notify_calls)


if __name__ == "__main__":
    unittest.main()