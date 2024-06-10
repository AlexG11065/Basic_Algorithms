from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    #  реализовать итеративный алгоритм бинарного поиска
    #
    #     low = 0
    #     high = len(seq) - 1
    #
    #     while low <= high:
    #         mid = (low + high) // 2
    #         guess = seq[mid]
    #
    #         if guess == value:
    #             return mid
    #         if guess > value:
    #             high = mid + 1
    #         else:
    #             low = mid - 1
    #         raise ValueError("Искомый элемент не найден")

    lew = 0
    right = len(seq) - 1

    while lew <= right:
        mid_index = lew + (right - lew) // 2
        mid_value = seq[mid_index]

        if value == mid_value:
            while True:
                if not 0 <= mid_index - 1 < len(seq) or seq[mid_index - 1] != value:
                    break
                else:
                    mid_index -= 1
            return mid_index

        elif mid_value < value:
            lew = mid_index + 1

        else:
            right = mid_index - 1

    raise ValueError("Искомый элемент не найден")


if __name__ == "__main__":
    print(binary_search(5, [i for i in range(1, 51)]))  # 4 index
    print(binary_search(31, [i for i in range(1, 51)]))  # 30 index
    print(binary_search(52, [i for i in range(1, 51)]))  # ValueError("Искомый элемент не найден")
