"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.


Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # expected = sum(range(len(nums) + 1))
        """Above will run fine. Below is much faster since we have a constraint that array will always start with 0 and
        len(array) is O(1)"""
        n = len(nums)
        expected = (n * (n + 1)) // 2  # / will give 12.0 // will give just 12
        return expected - sum(nums)


class MissingNumberTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test_missing_number(self):
        func = self.obj.missingNumber
        self.assertEqual(func([3, 0, 1]), 2)
        self.assertEqual(func([0, 1]), 2)
        self.assertEqual(func([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)


if __name__ == "__main__":
    main()
