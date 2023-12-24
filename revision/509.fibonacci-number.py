#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (70.51%)
# Likes:    7781
# Dislikes: 339
# Total Accepted:    1.6M
# Total Submissions: 2.3M
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
# 
# 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# 
# 
# Given n, calculate F(n).
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 30
# 
# 
#

# @lc code=start
class Solution:
    # def __init__(self):
    #     self.cache = {}
        
    def fib(self, n: int) -> int:
      
        #Bruteforce
        # if(n == 1 ):
        #     return 1
        # if(n == 0 ):
        #     return 0
        # return self.fib(n-1) + self.fib(n-2)

        #Top-down recursion DP memoisation
        # if(n == 1 ):
        #     return 1
        # elif(n == 0 ):
        #      return 0
        # if n in self.cache :
        #     return self.cache[n]
        # self.cache[n] =  self.fib(n-1) + self.fib(n-2)
        # return self.cache[n]


        #bottom up approach
        if(n == 1 ):
            return 1
        elif(n == 0 ):
             return 0
        i =2
        data = [0] * (n+1)
        data[0] = 0
        data[1] = 1
        j = 2
        while(i<=n):
            temp = data[1]
            data[1] = data[0] + data[1]
            data[0] = temp

            # using more mem
            # data[j] = data[j-1] + data[j-2]

            i += 1
        return data[1]
        
# @lc code=end

