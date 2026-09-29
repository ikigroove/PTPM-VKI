from src.triangle import Triangle
from src.database import Database
from src.email_notificaton import EmailNotificationService

class Controller:
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.database = Database()
        self.notification_service = EmailNotificationService()

    def run(self):
        a, b, c = 0.0, 0.0, 0.0

        try:
            a, b, c = self.user_interface.get_triangle_sides()
            triangle = Triangle(a, b, c)
            triangle.process()
        except (ValueError, TypeError) as e:
            triangle = Triangle(0.0, 0.0, 0.0)
            triangle.coordinates = [(-2, -2), (-2, -2), (-2, -2)]
            triangle.err_msg = "Ошибка ввода: " + str(e)

        self.database.insert_triangle(a, b, c, triangle.triangle_type, triangle.err_msg)

        self.notification_service.notify(f"Тип треугольника: {triangle.triangle_type}")
        self.notification_service.notify(f"Координаты вершин: {triangle.coordinates}")
        self.notification_service.notify(f"Сообщение об ошибке: {triangle.err_msg}")