"""
Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

"""


def flatten(arr):
    result = []
    if len(arr) >= 1:
        if isinstance(arr[0], list):
            result.extend(flatten(arr[0]))
        else:
            result.append(arr[0])
        if len(arr) > 1:
            result.extend(flatten(arr[1:]))
    return result

# Examples
print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))
