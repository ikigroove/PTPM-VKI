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

            cached = self.database.find_triangle(a, b, c)
            if cached is not None:
                triangle_type, err_msg = cached
                triangle = Triangle(a, b, c)
                triangle.triangle_type = triangle_type
                triangle.err_msg = err_msg or ""
            else:
                triangle = Triangle(a, b, c)
                triangle.process()
                self.database.insert_triangle(
                    a, b, c, triangle.triangle_type, triangle.err_msg
                )
        except (ValueError, TypeError) as e:
            triangle = Triangle(0.0, 0.0, 0.0)
            triangle.err_msg = "Ошибка ввода: " + str(e)

            if cached is None:
                self.database.insert_triangle(
                    0.0, 0.0, 0.0, triangle.triangle_type, triangle.err_msg
                )
            else:
                triangle.triangle_type, triangle.err_msg = cached[0], cached[1] or ""

        self.notification_service.notify(f"Тип треугольника: {triangle.triangle_type}")
        self.notification_service.notify(f"Сообщение об ошибке: {triangle.err_msg}")