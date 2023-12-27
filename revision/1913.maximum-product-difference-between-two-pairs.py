#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
#
# algorithms
# Easy (83.03%)
# Likes:    1452
# Dislikes: 63
# Total Accepted:    217.5K
# Total Submissions: 262.1K
# Testcase Example:  '[5,6,2,7,4]'
#
# The product difference between two pairs (a, b) and (c, d) is defined as (a *
# b) - (c * d).
# 
# 
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2
# * 7) = 16.
# 
# 
# Given an integer array nums, choose four distinct indices w, x, y, and z such
# that the product difference between pairs (nums[w], nums[x]) and (nums[y],
# nums[z]) is maximized.
# 
# Return the maximum such product difference.
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and
# indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,2,5,9,7,4,8]
# Output: 64
# Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and
# indices 1 and 5 for the second pair (2, 4).
# The product difference is (9 * 8) - (2 * 4) = 64.
# 
# 
# 
# Constraints:
# 
# 
# 4 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
# 
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m1 = self.findmax(nums)
        m2 = self.findmax(nums)
        mi1 = self.findmin(nums)
        mi2 = self.findmin(nums)

        return(m1*m2) - (mi1*mi2)


    def findmax(self,nums) :
        themaxnum = max(nums)
        nums.remove(themaxnum)
        return themaxnum

    def findmin(self,nums) : 
        theminnum = min(nums)
        nums.remove(theminnum)
        return theminnum
# @lc code=end

