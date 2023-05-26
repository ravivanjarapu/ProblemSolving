"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.



Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"


Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
"""

from unittest import TestCase, main


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return str(0)

        # Exclusive OR - Both of them being True returns False
        result = '-' if (numerator < 0) ^ (denominator < 0) else ''

        numerator, denominator = abs(numerator), abs(denominator)
        result += str(numerator // denominator)
        remainder = numerator % denominator

        if remainder == 0:
            return result
        result += '.'

        remainder = numerator % denominator
        remainder_dict = {}
        while remainder != 0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        if remainder == 0:
            return result
        return result[:remainder_dict[remainder]] + '(' \
            + result[remainder_dict[remainder]:] + ')'


class FractionTester(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = Solution()

    def test_1(self):
        result = self.obj.fractionToDecimal(-50, 8)
        self.assertEqual(result, "-6.25")


if __name__ == '__main__':
    main()
