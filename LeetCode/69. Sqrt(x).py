"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """        NEWTON-RAPHSON METHOD
        FORMULA --> x'n+1' = 1/2(x'n' + N/x'n') where N is the input to which we have to find sq rt
        We declare X'n+1' as ; and x'n' as 'a' to avoid confusion
        b = 1/2(a + (N/a))
        """
        if x <= 1:
            return x
        prev_result = x / 2
        result = (prev_result + (x / prev_result)) / 2

        while int(result) != int(prev_result):
            prev_result = result
            result = (result + (x / result)) / 2
        return int(result)


obj = Solution()
print(obj.mySqrt(32))
print(obj.mySqrt(8))
