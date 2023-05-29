"""Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    """
    Leetcode Hint: If the temperature is say, 70 today, then in the future a warmer temperature must be either 71,
    72, 73, ..., 99, or 100. We could remember when all of them occur next.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #  O(n) time and O(n) space
        # https://www.youtube.com/watch?v=cTBiBSnjO3c -- Neetcode
        answer = [0] * len(temperatures)
        stack = []  # pair: (temperature: index)
        for i, temperature in enumerate(temperatures):
            while stack and (stack[-1][0] < temperature):
                last_highest_temp, last_highest_temp_index = stack.pop()
                answer[last_highest_temp_index] = i - last_highest_temp_index
            stack.append((temperature, i))

        return answer
