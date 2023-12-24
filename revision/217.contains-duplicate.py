#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums :
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for key,val in dict.items() : 
            if val > 1 : 
                return True
            
        return False
        
# @lc code=end

