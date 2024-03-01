#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for n in nums : 
            dict[n] = dict.get(n,0) + 1
        for k,v in dict.items() : 
            if(v>1):
                return True

            
        
# @lc code=end

