import math

from typing import Any, List
from copy import deepcopy


# time - O(log n)
# space - O(1)
def jump_search(arr: List[Any], val: Any) -> int:
    step = int(math.sqrt(len(arr)))
    res = -1

    prev = 0
    while prev + step - 1 <= len(arr) - 1:
        if arr[prev + step - 1] == val:
            return prev + step - 1
        if arr[prev + step - 1] > val:
            break
        prev += step

    while prev <= prev + step and prev <= len(arr) - 1:
        if arr[prev] == val:
            res = prev
            break
        prev += 1
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert jump_search(arr, 5) == 4
    assert jump_search(arr, 13) == 12
    assert jump_search(arr, 200) == -1
    assert jump_search(arr, 1) == 0
    assert jump_search([1], 1) == 0