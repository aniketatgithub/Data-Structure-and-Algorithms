#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (60.75%)
# Likes:    30682
# Dislikes: 464
# Total Accepted:    1.9M
# Total Submissions: 3.1M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l =0 
        maxl , maxr = 0, 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                waterL = maxl - height[l]
                if  waterL > 0 :
                    res += waterL 
                maxl = max(maxl,height[l])
                l+=1

            else : 
                waterL = maxr - height[r]
                if  waterL > 0 :
                    res += waterL 
                maxr = max(maxr,height[r])
                r-=1

        return res
# @lc code=end

