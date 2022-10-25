'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            for i, source_letter in enumerate(strs[0]):
                # print('Source letter: %s' % source_letter)
                for target_str in strs[1:]:
                    # print('Target String: %s' % target_str)
                    if len(target_str) <= i or source_letter != target_str[i]:
                        return strs[0][:i]
        return strs[0]


obj = Solution()
strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]
strs = ["dog"]
strs = [""]
strs = ["flower", "flower", "flower", "flower"]
print(obj.longestCommonPrefix(strs))
