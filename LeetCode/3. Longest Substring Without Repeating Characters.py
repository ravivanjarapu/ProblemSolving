"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)
        maxlength, lp = 0, 0
        charSet = set()
        for rp, val in enumerate(s):  # O(n)
            while val in charSet:  # O(n)
                charSet.remove(s[lp])
                lp += 1
            charSet.add(val)
            maxlength = max(maxlength, rp - lp + 1)
        return maxlength


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("abba"))
print(Solution().lengthOfLongestSubstring("tmmzuxt"))

