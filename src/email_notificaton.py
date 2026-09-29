from src.abstract.notification_service import NotificationService

class EmailNotificationService(NotificationService):
    def notify(self, message: str) -> None:
        print(f"Отправка уведомления по электронной почте: {message}")