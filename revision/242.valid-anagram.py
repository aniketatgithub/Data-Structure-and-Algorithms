#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (64.28%)
# Likes:    11733
# Dislikes: 377
# Total Accepted:    3.2M
# Total Submissions: 5M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs, ht= {},{}
        if len(s) != len(t):
            return False
        for c in range(len(s)):
            hs[s[c]] = hs.get(s[c],0) + 1
            ht[t[c]] = ht.get(t[c],0) + 1
        for c in hs : 
            if hs[c] != ht.get(c,0):
                return False
        return True
# @lc code=end

