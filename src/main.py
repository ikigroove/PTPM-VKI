from logger import Logger
from triangle import Triangle

def main() -> None:
    logger = Logger.setup()

    try:
        a = float(input("Введите длину стороны A: "))
        b = float(input("Введите длину стороны B: "))
        c = float(input("Введите длину стороны C: "))

        triangle = Triangle(a, b, c, logger)
        triangle.process()

    except (ValueError, TypeError) as e:
        logger.error(f"Ошибка ввода: {e}")
        triangle = Triangle(0, 0, 0, logger)
        triangle.coordinates = [(-2, -2), (-2, -2), (-2, -2)]

    print(f"\nТип треугольника: {triangle.triangle_type}")
    print(f"Координаты вершин: {triangle.coordinates}")


if __name__ == "__main__":
    main()