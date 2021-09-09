def combinations(arr, M):
    """
    arr 배열에서 M개의 조합을 리턴한다
    """

    if M == 0:
        return [[]]

    elif M == 1:
        return [[item] for item in arr]

    result = []

    for index, value in enumerate(arr[: -M + 1 :]):
        for combo in combinations(arr[index + 1 : :], M - 1):
            result += [[value] + combo]

    return result
