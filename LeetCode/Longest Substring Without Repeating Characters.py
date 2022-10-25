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
        if len(s) == 0:
            return 0
        maxlength, lp = 0, 0

        # O(n^2)
        # charSet = set()
        # for rp, val in enumerate(s): # O(n)

        #     while val in charSet:   # O(n)
        #         charSet.remove(s[lp])
        #         lp += 1
        #         charSet.add(val)
        #     maxlength = max(maxlength, lp - rp + 1)

        # O(n)
        indexDict = {}
        print(dict(enumerate(s)), '\n')
        for rp, val in enumerate(s):
            if val in indexDict:
                # lp = indexDict[val] + 1
                lp = max(lp, indexDict[val] + 1)

            indexDict[val] = rp
            maxlength = max(maxlength, rp - lp + 1)

            # print(indexDict)
            # print('lp: ', lp, end='')
            # print(' rp: ', rp)
            # print('maxlength: %d' % maxlength)
            # print('\n')
        return maxlength


# print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("abba"))
print(Solution().lengthOfLongestSubstring("tmmzuxt"))


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         dicts = {}
#         maxlength = start = 0
#         for i,value in enumerate(s):
#             if value in dicts:
#                 sums = dicts[value] + 1
#                 if sums > start:
#                     start = sums
#             num = i - start + 1
#             if num > maxlength:
#                 maxlength = num
#             dicts[value] = i
#         return maxlength
