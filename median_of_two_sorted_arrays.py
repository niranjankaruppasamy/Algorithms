def find_median(arr1: list, arr2: list) -> float:
    tot = len(arr1) + len(arr2)
    if tot%2 == 1:
        mid = tot//2
    else:
        mid = tot//2, tot//2 + 1
    for _ in range(max(len(arr1), len(arr2))):
        pass


if __name__ == "__main__":
    assert find_median([1, 3], [2]) == 2.0
    assert find_median([1, 2], [3, 4]) == 2.5