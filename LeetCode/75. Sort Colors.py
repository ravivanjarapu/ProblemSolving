"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wp, bp = -1, -1
        if nums[0] == 1:
            wp = 0
        elif nums[0] == 2:
            bp = 0
        for i in range(1, len(nums)):
            if (nums[i] == 2) or (nums[i] >= nums[i - 1]):
                continue
            # if nums[i] == 0:
            #     if rp < 0:
            #         nums[0], nums[i] = nums[i], nums[0]
            #         rp = 0
            #         if nums[i] == 1:
            #             wp = i
            #         elif nums[i] == 2:
            #             bp = i
            # if nums[i] == 1:
            #     bp += 1
            #     nums[bp-1], nums[i] = nums[i], nums[bp-1]
            #     if nums[bp - 1] == 0:
            #         wp = i
            if nums[i] == 0:
                if wp >= 0:
                    nums[wp], nums[i] = nums[i], nums[wp]
            elif nums[i] == 1:
                if wp < 0:
                    wp = i
                elif wp > bp:
                    wp = bp
            if bp >= 0:
                nums[i], nums[bp] = nums[bp], nums[i]
                bp += 1
            print(nums, 'i: ', i, 'wp: ', wp, 'bp: ', bp)

obj = Solution()
input_nums = [2,0,2,1,1,0]
obj.sortColors(input_nums)
print(input_nums)
