from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    x = set(nums1)
    y = set(nums2)
    result = x.intersection(y)
    return list(result)


if __name__ == "__main__":
    n = [1, 2, 2, 1]
    m = [2, 2]
    print(intersection(n, m))
