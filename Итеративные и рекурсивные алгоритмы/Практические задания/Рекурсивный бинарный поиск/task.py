from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    # TODO реализовать алгоритм бинарного поиска

    if right_border is None:
        right_border = len(seq) - 1

    while left_border <= right_border:
        mid = (left_border + right_border) // 2
        guess = seq[mid]
        if guess == value:
            return mid

        if guess > value:
            right_border = mid - 1
        else:
            left_border = mid + 1

    raise ValueError(f"Значение {value} не найдено")


if __name__ == "__main__":
    seq = [1, 2, 2, 2, 2, 2]
    print(seq)
    # seq = [a for a in range(1, 51)]
    print(binary_search(2, seq))
    print(binary_search(10, seq))
    print(binary_search(-1, seq))
