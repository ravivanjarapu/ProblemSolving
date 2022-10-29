"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Sliding window concept
        if needle and haystack:
            for i in range(len(haystack)):
                print('Comparing ', haystack[i:i+len(needle)], ' with ', needle)
                if len(haystack[i:]) < len(needle):
                    break
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1


obj = Solution()
haystack, needle = "sadbutsad", "sad"
# haystack, needle = "leetcode", "leeto"
haystack, needle = "mississippi", "issip"
print(obj.strStr(haystack, needle))