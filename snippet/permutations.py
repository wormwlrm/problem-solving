def permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for index, elem in enumerate(arr):
        # arr[index::]로 하면 중복 가능
        for perm in permutations(arr[:index:] + arr[index + 1 : :], n - 1):
            result += [[elem] + perm]

    return result
