class Converter:

    @staticmethod
    def do(x: float) -> int:
        if (x * 10) % 1 != 0:
            raise ValueError(f"Invalid float precision: {x!r}. Expected at most 1 decimal place")

        if x >= 100.7:
            return 1000
        elif x > 0 and x < 100.7:
            return int(x)
        elif x == 0.0:
            raise ValueError(f"Invalid argument: value cannot be exactly zero.")
        elif x >= -30.4 and x < 0:
            return int(x) - 5
        elif x <= -30.5:
            return -2000


def main():
    x = float(input())
    print(Converter.do(x))

if __name__ == "__main__":
    main()

# x ∈ [100.7; + ∞) -> метод возвращает число 1000.
# x ∈ (0; 100.7) -> метод возвращает целую часть числа x путем отбрасывания дробной части (эквивалентно int(x)).
# x == 0.0 -> генерируется исключение ValueError (аналог ArgumentException).
# x ∈ [-30.4; 0) -> метод возвращает целую часть числа x путем отбрасывания дробной части (эквивалентно int(x)) минус 5.
# x ∈ (-∞ ; -30.5] -> метод возвращает число -2000.