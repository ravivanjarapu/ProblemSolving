"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for i in nums:
            if i - 1 not in nums_set:
                # Sequence starts here
                sequence_length = 1
                temp = i + 1
                while i + sequence_length in nums_set:
                    sequence_length += 1
                    temp += 1
                max_length = max(sequence_length, max_length)
        print('max_length: ', max_length)
        return max_length


class PriceTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test1(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.obj.longestConsecutive(nums), 4)

    def test2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEqual(self.obj.longestConsecutive(nums), 9)


if __name__ == "__main__":
    main()
