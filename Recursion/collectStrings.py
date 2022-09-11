"""Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string."""

def collectStrings(obj):
    result = []
    for key, val in obj.items():
        if isinstance(val, str):
            result.append(val)
        elif isinstance(val, dict):
            result.extend(collectStrings(val))
    return result


obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

print(collectStrings(obj)) # ['foo', 'bar', 'baz']