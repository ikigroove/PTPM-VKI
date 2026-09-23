import logging

class Triangle:

    def __init__(self, a: float, b: float, c: float, logger: logging.Logger):
        self.a = a
        self.b = b
        self.c = c
        self.logger = logger
        self.triangle_type = "не треугольник"
        self.coordinates = [(-1, -1), (-1, -1), (-1, -1)]

    def _is_valid_sides(self) -> bool:
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            self.logger.error("Длины сторон должны быть положительными числами.")
            return False
        return True

    def _is_triangle_inequality(self) -> bool:
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            self.logger.error("Не является треугольником")
            return False
        return True

    def _classify(self) -> None:
        if self.a == self.b == self.c:
            self.triangle_type = "равносторонний"
            self.logger.info("Равносторонний треугольник")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            self.triangle_type = "равнобедренный"
            self.logger.info("Равнобедренный треугольник")
        elif self.a != self.b != self.c:
            self.triangle_type = "разносторонний"
            self.logger.info("Разносторонний треугольник")

    def reset_coordinates(self) -> None:
        self.coordinates = [(-2, -2), (-2, -2), (-2, -2)]
        self.triangle_type = ""

    def _calculate_coordinates(self) -> None:
        c, b, a = self.c, self.b, self.a
        x = (c ** 2 + b ** 2 - a ** 2) / (2 * c)
        y = (b ** 2 - x ** 2) ** 0.5
        self.coordinates = [(0, 0), (c, 0), (x, y)]

    def process(self) -> None:
        if not self._is_valid_sides():
            return
        if not self._is_triangle_inequality():
            return
        self._classify()
        self._calculate_coordinates()