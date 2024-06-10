from typing import List


def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    # return s


if __name__ == "__main__":
    v = ["н", "о", "л", "с"]
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [i for i in range(20)]
    reverse_string(b)
    print(b)
    reverse_string(v)
    reverse_string(a)
    print(a)
    print(v)

