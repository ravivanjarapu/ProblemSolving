"""Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized."""




def capitalizeWords(arr):
    result = []
    if len(arr) != 0:
        result.append(arr[0].upper())
    if len(arr) > 1:
        result.extend(capitalizeWords(arr[1:]))
    return result


# Examples
words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']