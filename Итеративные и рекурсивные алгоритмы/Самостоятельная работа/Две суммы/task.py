from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> List[int]:
    for index1, value1 in enumerate(nums):
        for index2, value2 in enumerate(nums):
            if value1 + value2 == target and index1 != index2:
                return [index1, index2]


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4, 5, 6], 5))


def two_sum2(nums: List[int], target: int) -> tuple[int, int]:
    result = {}
    for index, value in enumerate(nums):
        result[target - value] = index
    for index, value in enumerate(nums):
        if value in result:
            return result[value], index


print(two_sum2([1, 2, 3, 4, 5, 6], 5))
