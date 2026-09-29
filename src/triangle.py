class Triangle:

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        self.triangle_type = "не треугольник"
        self.coordinates = [(-1, -1), (-1, -1), (-1, -1)]
        self.err_msg = ""

    def _is_valid_sides(self) -> bool:
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            self.err_msg = "Стороны треугольника должны быть положительными"
            return False
        return True

    def _is_triangle_inequality(self) -> bool:
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            self.err_msg = "Стороны не удовлетворяют неравенству треугольника"
            return False
        return True

    def _classify(self) -> None:
        if self.a == self.b == self.c:
            self.triangle_type = "равносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            self.triangle_type = "равнобедренный"
        elif self.a != self.b != self.c:
            self.triangle_type = "разносторонний"

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