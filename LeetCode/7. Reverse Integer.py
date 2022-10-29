"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x != 0:
            number_to_reverse = x
            if x < 0:
                number_to_reverse = abs(x)
            while number_to_reverse:
                temp_result = result * 10
                if temp_result > (2 ** 31) - 1:
                    return 0

                number_to_reverse, remainder = number_to_reverse // 10, number_to_reverse % 10

                if (temp_result == (2 ** 31) - 1) and (remainder > 7):
                    # max possible multiple of 10 below 2147483647 is 2147483640. So minimum possible overflow starts
                    # from 8
                    return 0

                result = remainder + temp_result
                print('quotient: ', number_to_reverse)
            if x < 0:
                result = -result
            if not -(2 ** 31) <= result <= (2 ** 31) - 1:
                return 0
        return result


obj = Solution()
print(obj.reverse(123))
print(obj.reverse(-123))
print(obj.reverse(120))
