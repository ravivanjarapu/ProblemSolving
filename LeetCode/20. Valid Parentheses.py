"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif c in ']})':
                try:
                    current_bracket = stack.pop()
                except IndexError:
                    return False
                if reference.get(c) != current_bracket:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False

        return True


obj = Solution()
print(obj.isValid("()[]{}"))
print(obj.isValid("(]"))
print(obj.isValid("()"))
print(obj.isValid("["))
print(obj.isValid(""))
print(obj.isValid("]"))
