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
    # не прошла проверку
    # if right_border is None:
    #     right_border = len(seq) - 1
    #
    # while left_border <= right_border:
    #     mid = (left_border + right_border) // 2
    #     guess = seq[mid]
    #     if guess == value:
    #         return mid
    #
    #     if guess > value:
    #         right_border = mid - 1
    #     else:
    #         left_border = mid + 1
    #
    # raise ValueError(f"Значение {value} не найдено")

    if right_border is None:
        right_border = len(seq) - 1

    if left_border > right_border:
        raise ValueError(f"Значение {value} не найдено")

    middle_index = left_border + (right_border - left_border) // 2
    middle_value = seq[middle_index]

    if value == middle_value:
        # while True:
        #     if not 0 <= middle_value - 1 <= len(seq) or seq[middle_value - 1] != value:
        #         break
        #     else:
        #         middle_value -= 1
        # return middle_index
        while 0 <= middle_index - 1 <= len(seq) and seq[middle_index - 1] == value:
            middle_index -= 1
        return middle_index

    elif middle_value < value:
        left_border = middle_index + 1

    else:
        right_border = middle_index - 1

    return binary_search(value, seq, left_border, right_border)


if __name__ == "__main__":
    print(binary_search(37, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]))
    # seq = [1, 2, 2, 2, 2, 2]
    # print(seq)
    # # seq = [a for a in range(1, 51)]
    # print(binary_search(2, seq))
    # print(binary_search(10, seq))
    # print(binary_search(-1, seq))
