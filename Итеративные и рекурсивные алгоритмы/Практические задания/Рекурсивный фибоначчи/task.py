import functools

count = 0
cache = {'count': 0}


@functools.lru_cache()
def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """

    # global count
    if n < 0:
        raise ValueError("Номер числа Фибоначчи не может быть отрицательным")
    global count
    if n == 0:
        count += 1
        # cache[n] = 0
        return 0
    if n == 1:
        count += 1
        return 1
    count += 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

    #  реализовать рекурсивный алгоритм


if __name__ == "__main__":
    print([fib_recursive(i) for i in range(10)])
    fib_recursive(10)
    print(count)
