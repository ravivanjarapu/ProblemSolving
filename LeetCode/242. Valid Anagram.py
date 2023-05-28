"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        return True if len(s) == len(t) and sorted(s) == sorted(t) else False:  # O( n log n ) time O(1) space
        return True if len(s) == len(t) and Counter(s) = Counter(t) else False:  # O( 2n ) time O(2n) space
        '''
        # Below is O(2n) time and O(1) space
        if len(s) == len(t):
            s_counter = Counter(s)  # This is O(1) space since max length is 26 (alphabet count)
            for i in t:
                s_counter[i] -= 1
                if s_counter[i] == -1:
                    return False
            return True
        return False