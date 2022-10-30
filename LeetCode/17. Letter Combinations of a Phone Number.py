"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letter_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 1:
            return list(letter_dict[digits[0]])
        result = []

        '''
        # This works for only 2 digits. When number of digits increases, we need to increase the number of loops
        which is not feasible because we don't want to edit code for every input
        first, second = letter_dict[digits[0]], letter_dict[digits[1]]
        for i in first:
            for j in second:
                result.append(i+j)'''
        # print('Current Digits: {}'.format(digits))
        first, second = letter_dict[digits[0]], digits[1:]

        for i in first:
            for j in self.letterCombinations(second):
                result.append(i + j)
        # print('result:', result)
        return result


obj = Solution()
print(obj.letterCombinations("234"))
# print(obj.letterCombinations(""))
print(obj.letterCombinations("2"))
