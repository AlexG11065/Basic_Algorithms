from typing import List
"""
Множество не содержит дубликаты элементов, пока не заглянул в доки не мог понять почему так))))
"""


def contains_duplicate(nums: List[int]) -> bool:
    print(len(set(nums)))
    return len(nums) > len(set(nums))


if __name__ == "__main__":
    n = [1, 2, 3, 4, 1]
    print(contains_duplicate(n))

