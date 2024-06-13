def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    str_s = list(s)
    str_s.sort()
    str_t = list(t)
    str_t.sort()
    return str_s == str_t


if __name__ == "__main__":

    m = "anagram"
    n = "nagarm"
    print(is_anagram(m, n)) # False




