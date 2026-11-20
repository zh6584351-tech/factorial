def factorial(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result