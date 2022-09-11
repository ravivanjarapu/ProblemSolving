"""Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!"""


def stringifyNumbers(obj):
    new_obj = {}
    for key, val in obj.items():
        if isinstance(val, dict):
            new_val = stringifyNumbers(val)
        elif str(val).isdigit():
            new_val = str(val)
        else:
            new_val = val
        new_obj[key] = new_val
    return new_obj


# Examples
obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringifyNumbers(obj))

# {'num': '1',
#  'test': [],
#  'data': {'val': '4',
#           'info': {'isRight': True, 'random': '66'}
#           }
#  }
