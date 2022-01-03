from typing import Any, List
from random import randint


def get_arr():
    arr = list()
    for _ in range(15):
        val = randint(10, 1000)
        arr.append(val)
    return arr

# linear time - O(n)
# efficient for unsorted array
def linear_search(arr: List[Any], val: Any) -> int:
    for ind, data in enumerate(arr):
        if data == val:
            return ind
    return -1


if __name__ == "__main__":
    arr = get_arr()
    assert linear_search(arr, arr[8]) == 8
    assert linear_search(arr, 1001) == -1