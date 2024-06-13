from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: Последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """

    if len(container) <= 1:
        return container

    pivot = container[0]  # выбираю опорный элемент
    lef = list(filter(lambda x: x < pivot, container))  # левая сторона, все что меньше опорного элемента
    centr = list(filter(lambda x: x == pivot, container))  # все что равно опорному элементу
    right = list(filter(lambda x: x > pivot, container))  # правая сторона, все что больше опорного элемента

    return sort(lef) + centr + sort(right)


#  реализовать алгоритм быстрой сортировки


if __name__ == "__main__":
    print(sort([2, 4, 6, 1, 2, 5, 7, 5, 4, 3, 2, 2, -1, -10, 3, 5, 56, 7, 8, 9, 99, 7, 65, 4, 3, 2]))
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([-1, 2, 5, 4]) == [-1, 2, 4, 5]
