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

    # pivot = container[0]  # выбираю опорный элемент container[len(container) // 2]
    pivot = container[len(container) // 2]
    lef = list(filter(lambda x: x < pivot, container))  # левая сторона, все что меньше опорного элемента
    centre = list(filter(lambda x: x == pivot, container))  # все что равно опорному элементу
    right = list(filter(lambda x: x > pivot, container))  # правая сторона, все что больше опорного элемента

    return sort(lef) + centre + sort(right)


#  реализовать алгоритм быстрой сортировки


if __name__ == "__main__":
    print(sort([2, 4, 6, 1, 2, 5, 7, 5, 4, 3, 2, 2, -1, -10, 3, 5, 56, 7, 8, 9, 99, 7, 65, 4, 3, 2]))
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([-1, 2, 5, 4]) == [-1, 2, 4, 5]


def portion(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def sort2(container: List[int]) -> List[int]:
    def _sort2(container, low, high):
        if low < high:
            pivot_index = portion(container, low, high)
            _sort2(container, low, pivot_index - 1)
            _sort2(container, pivot_index + 1, high)

    return _sort2(container, 0, len(container) - 1)



arr = [5,6,4,3,27,8,0,8,64,3,2,356,23]
print(portion(arr))
print(arr)
sort(arr)
print(arr)
