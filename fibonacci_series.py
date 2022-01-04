def fibonacci_series(num):
    arr = [0 for _ in range(num+1)]
    arr[0] = 0
    arr[1] = 1
    if num <= 1:
        return arr[num]
    for i in range(2, num+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[num]


if __name__ == "__main__":
    assert fibonacci_series(1) == 1
    assert fibonacci_series(10) == 55