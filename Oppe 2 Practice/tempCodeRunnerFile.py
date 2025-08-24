# 1)  Basic Number checks

def is_even_two_digit(num: int) -> bool:
    n = abs(num)
    return 10 <= n <= 99 and n % 2 == 0
