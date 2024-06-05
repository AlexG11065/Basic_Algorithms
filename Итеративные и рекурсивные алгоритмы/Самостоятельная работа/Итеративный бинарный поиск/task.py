from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать итеративный алгоритм бинарного поиска

    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = seq[mid]

        if guess == value:
            return mid
        if guess > value:
            high = mid + 1
        else:
            low = mid - 1
        raise ValueError("Искомый элемент не найден")

