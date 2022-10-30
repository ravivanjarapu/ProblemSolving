"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        result = []
        temp = []

        def get_next(open_p=0, close_p=0):
            if open_p == close_p == n:
                result.append(''.join(temp))
            if open_p < n:
                temp.append('(')
                get_next(open_p + 1, close_p)
                temp.pop()
            if close_p < open_p:
                temp.append(')')
                get_next(open_p, close_p + 1)
                temp.pop()

        get_next()
        return result


obj = Solution()
print(obj.generateParenthesis(4))
