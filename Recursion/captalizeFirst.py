"""Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array."""

def capitalizeFirst(arr):
    new_arr = []
    if len(arr) == 0:
        return new_arr
    word = arr[0]
    new_word = word[0].upper() + word[1:]
    new_arr.append(new_word)
    if len(arr) > 1:
        new_arr.extend(capitalizeFirst(arr[1:]))
    return new_arr


 # Example
print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']