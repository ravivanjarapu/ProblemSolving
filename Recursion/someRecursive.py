def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    print('Checking ', arr)
    if len(arr) != 0:
        result = cb(arr[0])
        if len(arr) > 1:
            result = result or someRecursive(arr[1:], cb)
        return result
    return False

print(someRecursive([4, 6, 8], isOdd))
