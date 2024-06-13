from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    if isinstance(nums, float):
        raise TypeError("Должен быть целочисленным числом")


if __name__ == "__main__":
    lst = [1, 2, 3, 5]
    for i, j in enumerate(lst):
        print(i,)

