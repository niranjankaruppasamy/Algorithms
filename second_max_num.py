import random


def create_array() -> list:
    arr = list()
    for _ in range(20):
        arr.append(random.randrange(10, 999))
    return arr

def find_second_max(arr: list) -> int:
    first_max = second_max = 0
    for _, data in enumerate(arr):
        if not first_max:
            first_max = data
            continue
        if data > first_max:
            second_max = first_max
            first_max = data
            continue
        if data > second_max:
            second_max = data

    return second_max

if __name__ == "__main__":
    arr = create_array()
    result = find_second_max(arr)
    print(arr, result)
