# actual, expected, order


def verify(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def print_logs(call_function):
    test_cases = [
        ([1, 10, 23, 50, 4, 9, -4], [-4, 1, 4, 9, 10, 23, 50], True)
        # ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], True),
        # ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1], False),
        # ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], False),
        # ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
    ]
    for idx, test_case in enumerate(test_cases):
        result = call_function(test_case[0], test_case[2])
        is_march = verify(test_case[1], result)
        print(result)

        log_str = f"{idx + 1}, actual: {test_case[0]}, expected: {test_case[1]} received: {result} pass: {is_march}"
        if not is_march:
            color_decorator = f'\x1b[31m{log_str}\x1b[0m'
            print(color_decorator)
        else:
            print(log_str)
