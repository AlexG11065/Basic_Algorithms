from typing import List


def missing_number(nums: List[int]) -> int:
    number = len(nums)
    total = number * (number + 1) // 2
    lacking = total - sum(nums)
    return lacking


if __name__ == "__main__":
    pass
