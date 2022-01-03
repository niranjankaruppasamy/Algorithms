def find_largest_sum_of_subarray(arr):
    max_until_here = arr[0]
    max_so_far = arr[0]
    for item in arr[1:]:
        max_until_here = max(item, max_until_here+item)
        max_so_far = max(max_so_far, max_until_here)
    return max_so_far


if __name__ == "__main__":
    # time = O(n)
    # space = O(1)
    assert find_largest_sum_of_subarray([1, 2, -3, 4, -5, 7, -2]) == 7