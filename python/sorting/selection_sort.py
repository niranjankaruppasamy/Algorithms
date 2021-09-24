from typing import List


# time - O(n^2)
# space - O(1)
def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min_val: int = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j
        if min_val != i:
            arr[min_val], arr[i] = arr[i], arr[min_val]
    return arr


if __name__ == "__main__":
    arr = [98, 4, 2, 7, 5, 10, 33, 1]
    str_arr = ['z', 'y', 'x', 'w', 'v', 'u']
    assert selection_sort(arr) == [1, 2, 4, 5, 7, 10, 33, 98]
    assert selection_sort(str_arr) == ['u', 'v', 'w', 'x', 'y', 'z']
