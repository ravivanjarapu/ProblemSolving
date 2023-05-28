"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List
from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        ****This is new solution created from scratch all by myself.*****
        """

        """
        https://leetcode.com/problems/product-of-array-except-self/solutions/3571841/beats-993-213-ms-python3-28-may-2023/ 
        Intuition: 
            Find product of all elements using a loop and then divide each element to remove it from 
            product and add to result

        Approach: 
            1. Find product of all elements using a loop and call it full_product. 
            2. Divide full_product by 
            each element to remove it from product and append to result 
            3. During the process of full_product 
            calculation, count the number of zeroes. If its more than 1, then all the elements of result array will be 
            zeroes 
            4. If only one zero is found in input array, do not multiple the full_product with that zero. The 
            product of all remaining elements will be in that position only. All remaining positions will be zeroes 
            Complexity 
        
        Time complexity: O(2n) --> O(n) in worst case
        Space complexity: O(1) --> Result array not included        
        """
        zeroes = 0
        full_product = 1
        for idx, i in enumerate(nums):
            if i == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0] * len(nums)
                position = idx
            else:
                full_product *= i
        if zeroes:
            result = [0] * len(nums)
            result[position] = full_product
        else:
            result = [full_product//i for i in nums]

        return result

