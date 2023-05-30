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

Leetcode Hint: If the temperature is say, 70 today, then in the future a warmer temperature must be either 71,
72, 73, ..., 99, or 100. We could remember when all of them occur next.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
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
        '''

        #  Below is O(n) time and O(1) space - We don't use extra space for stack like above
        # Explanation: https://globalsoftbay.blogspot.com/2023/05/leetcode-739-daily-temperatures.html
        length = len(temperatures)
        hottest = 0
        answer = [0] * length
        for curr_idx in range(length - 1, -1, -1):
            curr_temperature = temperatures[curr_idx]
            if curr_temperature >= hottest:
                hottest = curr_temperature
                continue

            days = 1
            while temperatures[curr_idx + days] <= temperatures[curr_idx]:
                days += answer[curr_idx + days]
            answer[curr_idx] = days
        return answer
