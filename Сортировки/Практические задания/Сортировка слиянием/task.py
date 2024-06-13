from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if len(container) > 1:
        center = len(container) // 2
        left = container[:center]
        right = container[center:]
        sort(left)
        sort(right)

        left_index = right_index = container_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                container[container_index] = left[left_index]
                left_index += 1
            else:
                container[container_index] = right[right_index]
                right_index += 1
            container_index += 1

        while left_index < len(left):
            container[container_index] = left[left_index]
            left_index += 1
            container_index += 1

        while right_index < len(right):
            container[container_index] = right[right_index]
            right_index += 1
            container_index += 1

    return container


#  реализуйте сортировку слиянием


if __name__ == "__main__":
    print(sort([2, 4, 5, 7, 85, 564, 678, 22, 4566]))
