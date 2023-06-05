"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # https: // www.youtube.com / watch?v = jSto0O4AJbM - NeetCode
        if t == '':
            return ''

        result = ''

        s_counter, t_counter = defaultdict(int), Counter(t)
        have, need = 0, len(t_counter)

        left = 0
        for right, char in enumerate(s):
            if char in t_counter:
                s_counter[char] += 1
                if s_counter[char] == t_counter[char]:
                    have += 1

                while have == need:
                    # Update the result
                    if (result == '') or (
                            (right - left + 1) < len(result)):
                        result = s[left:right + 1]

                    # pop from left
                    s_counter[s[left]] -= 1
                    if s[left] in t_counter and s_counter[s[left]] < t_counter[s[left]]:
                        have -= 1
                    left += 1
        return result


obj = Solution()
print('MWS: *', obj.minWindow(s="ADOBECODEBANC", t="ABC"), '*')
# print(obj.minWindow(s="a", t="a"))
# print(obj.minWindow("a", t="aa"))
