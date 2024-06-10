def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """

    if n < 0:
        raise ValueError("Номер числа Фибоначчи должен быть не отрицательным числом")
    a = 0
    b = 1

    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c

    #  написать итеративный алгоритм чисел Фибоначчи


if __name__ == "__main__":
    print(fib_iterative(10))
    print(fib_iterative(0))
    print(fib_iterative(1))
    print(fib_iterative(2))
    print(fib_iterative(3))
    print(fib_iterative(6))
    print([fib_iterative(i) for i in range(10)])
    # print(fib_iterative(-1))
