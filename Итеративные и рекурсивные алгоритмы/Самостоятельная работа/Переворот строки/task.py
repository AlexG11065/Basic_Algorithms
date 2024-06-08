from typing import List


def reverse_string(s: List[str]) -> None:
    reversed_list = s.reverse()
    return reversed_list


if __name__ == "__main__":
    v = ["н", "о", "л", "с"]
    print(reverse_string(v))
