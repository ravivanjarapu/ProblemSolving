"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # length = len(columnTitle)
        #
        result = 0
        # for i in range(length - 1, -1, -1):
        #     letter = columnTitle[length - 1 - i]
        #     ord_val = ord(letter) - 64  # ord(letter) - ord('A') + 1.  ord('A') is 65. So, - ord('A') + 1 is always 64
        #     result += ord_val * (26 ** i)


        '''The updated approach below should be faster than the previous implementation.
        Exponentiation can be a computationally expensive operation, especially for larger powers.
        In the updated approach, we avoid exponentiation and instead calculate the value iteratively by multiplying the 
        existing result by 26 and adding the value for the current letter. This approach eliminates the need for 
        exponentiation and reduces the number of mathematical operations required, making it more efficient in terms of 
        time complexity.'''
        for letter in columnTitle:
            result *= 26
            result += (ord(letter) - 64)
        return result


