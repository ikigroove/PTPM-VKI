import unittest
from unittest.mock import patch
from src.email_notificaton import EmailNotificationService

class TestNotificationService(unittest.TestCase):

    @patch('builtins.print')
    def test_notify(self, mock_print):
        service = EmailNotificationService()

        service.notify('тестовое сообщение')

        mock_print.assert_called_once_with('Отправка уведомления по электронной почте: тестовое сообщение')


if __name__ == "__main__":
    unittest.main()