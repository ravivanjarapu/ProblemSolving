"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,
and if the quotient is strictly less than -2^31, then return -2^31.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # if the quotient is strictly less than the divisor, then division    will    fail    and returns the dividend    instead of  the divisor.
        # elif the quotient is strictly greater than the divisor, then division   will    fail    and
        # return the dividend    instead of  the divisor.
        # elif the quotient is greater than the divisor, then division   will    fail    and
        # return the dividend    instead of  the divisor.
        # elif the quotient is less than the divisor, then division   will    fail    and
        # return the dividend    instead of  the divisor.
        # else:
        # if dividend > divisor:
        #         return dividend - divisor
        #     elif dividend < divisor:
        #         return dividend + divisor
        #     else:
        #         return dividend
        #     class Solution:
        #         def divide(self, dividend: int, divisor: int) -> int:
        #             if dividend > divisor:
        #                 return dividend - divisor
        #             elif dividend < divisor:
        #                 return dividend + divisor
        #             else:
        #                 return dividend
        #             def __init__(self):
        #             self.dividend = 0
        #             self.divisor = 0
        #             self.quotient = 0
        denominator = abs(divisor)
        numerator = abs(dividend)
        result = 0
        print('\nChecking for dividend %d and divisor %d' % (dividend, divisor))
        '''
        # Time LIMIT exceeded
        while numerator >= denominator:
            print('Dividend: ', numerator)
            numerator -= denominator
            result += 1           
        '''
        while numerator >= denominator:
            print('Dividend: ', numerator)
            denominator_multiple = denominator
            times = 1
            while denominator_multiple <= numerator:
                numerator -= denominator_multiple
                result += times
                denominator_multiple += denominator_multiple
                times += times

        # if result > 2147483647:
        #     result = 2147483647
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            result = -result
        if result > 0:
            result = min(2147483647, result)
        else:
            result = max(result, -2147483648)
        return result


obj = Solution()
print(obj.divide(10, 3))
print(obj.divide(7, -3))
print(obj.divide(1, 1))
print(obj.divide(-2147483648, 1))
print(obj.divide(2147483648, 1))
