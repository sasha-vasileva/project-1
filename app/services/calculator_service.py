def is_leap_year(year: int) -> bool:
    """Возвращает True, если год високосный по правилам Григорианского календаря.

    Выбрасывает ValueError для года < 1.
    """
    if year < 1:
        raise ValueError('year must be >= 1')

    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
