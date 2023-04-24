"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
from functools import reduce
from typing import List
from unittest import TestCase, main


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


class SingleNumberTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test1(self):
        self.assertEqual(1, self.obj.singleNumber([2, 2, 1]))

    def test2(self):
        self.assertEqual(4, self.obj.singleNumber([4, 1, 2, 1, 2]))

    def test3(self):
        self.assertEqual(1, self.obj.singleNumber([1]))


if __name__ == '__main__':
    main()
