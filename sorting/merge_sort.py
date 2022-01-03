def merge_sort(arr: list) -> list:
    l = 0
    r = len(arr) - 1

    pass


if __name__ == "__main__":
    arr = [98, 4, 2, 7, 5, 10, 33, 1]
    str_arr = ['z', 'y', 'x', 'w', 'v', 'u']
    assert merge_sort(arr) == [1, 2, 4, 5, 7, 10, 33, 98]
    assert merge_sort(str_arr) == ['u', 'v', 'w', 'x', 'y', 'z']
