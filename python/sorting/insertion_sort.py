from typing import List


# time - O(n^2)
def insertion_sort(arr: List[int]) -> List[int]:
    i = 1
    while i < len(arr):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr


if __name__ == "__main__":
    arr = [98, 4, 2, 7, 5, 10, 33, 1]
    str_arr = ['z', 'y', 'x', 'w', 'v', 'u']
    assert insertion_sort(arr) == [1, 2, 4, 5, 7, 10, 33, 98]
    assert insertion_sort(str_arr) == ['u', 'v', 'w', 'x', 'y', 'z']
