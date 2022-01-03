def bubble_sort(arr):
    # best case - O(n), avg, worst case - O(n^2)
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [98, 4, 2, 7, 5, 10, 33, 1]
    str_arr = ['z', 'y', 'x', 'w', 'v', 'u']
    # compare the adjacent value
    assert bubble_sort(arr) == [1, 2, 4, 5, 7, 10, 33, 98]
    assert bubble_sort(str_arr) == ['u', 'v', 'w', 'x', 'y', 'z']
