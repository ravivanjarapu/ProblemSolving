"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104


Follow up: Could you write a solution that works in logarithmic time complexity?
"""
from unittest import TestCase, main


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        temp, multiplier = n / 10, n // 10
        decimal_part = temp - multiplier

        # additive = floor(decimal_part) if decimal_part < 0.5 else ceil(decimal_part)
        # Below line is same as above but without math imports
        additive = int(decimal_part + 0.5)

        return (multiplier * 2) + additive


class TrailingZeroesTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test_1(self):
        self.assertEqual(self.obj.trailingZeroes(1), 0)

    def test_5(self):
        self.assertEqual(self.obj.trailingZeroes(5), 1)

    def test_10(self):
        self.assertEqual(self.obj.trailingZeroes(10), 2)

    def test_14(self):
        self.assertEqual(self.obj.trailingZeroes(14), 2)

    def test_15(self):
        self.assertEqual(self.obj.trailingZeroes(15), 3)

    def test_trailingZeroes(self):
        self.assertEqual(self.obj.trailingZeroes(20), 4)
        self.assertEqual(self.obj.trailingZeroes(30), 7)


if __name__ == '__main__':
    main()
