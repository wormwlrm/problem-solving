def combinations(arr, M):
    if M == 0:
        return [[]]

    elif M == 1:
        return [[item] for item in arr]

    result = []

    # arr[::], arr[index::] 로 만들면 중복 허용
    for index, value in enumerate(arr[: -M + 1 :]):
        for combo in combinations(arr[index + 1 : :], M - 1):
            result += [[value] + combo]

    return result
