from typing import List


def majority_element(nums: List[int]) -> int:
    count = 0
    candidate = None
    for x in nums:
        if count == 0:
            candidate = x
            count += 1
        else:
            if x == candidate:
                count += 1
            else:
                count -= 1

    return candidate
