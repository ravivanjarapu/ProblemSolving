"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        counter = Counter(nums)
        # return [i[0] for i in counter.most_common(k)]
        """
        %timeit heapq.nlargest(2, count.keys(), key=count.get)
        2.78 µs ± 309 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
        
        %timeit [i[0] for i in count.most_common(2)]
        3.72 µs ± 397 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
        """
        return heapq.nlargest(k, counter.keys(), key=counter.get)
