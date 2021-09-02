from typing import Any, List


def binary_search_1(arr: List[Any], val:Any) -> int:
    # Iterative method
    # space - O(1)
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left+right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_2(arr: List[Any], val:Any, left:int, right:int) -> int:
    # Recursive method
    # space - O(n)
    mid = left + (right - left) // 2
    if left < right:
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return binary_search_2(arr, val, mid+1, right)
        else:
            return binary_search_2(arr, val, left, mid-1)
    return -1



if __name__ == "__main__":
    # we can acheive binary search by 2 methods.
    # iterative and recursive method
    # efficient for sorted arrays
    # time - O(log n)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert binary_search_1(arr, 7) == 6
    assert binary_search_1(arr, 100) == -1
    assert binary_search_2(arr, 8, 0, len(arr)-1) == 7
    assert binary_search_2(arr, 200, 0, len(arr)-1) == -1
