

# def isPalindrome(s):
#     print(s)
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# s = "abcdcba"
# print(isPalindrome(s))

# s= "Aniket"
# print(isPalindrome(s))

class Solution(object):
    def isPalindrome(self,s):
        str = ""
        for i in s:
            if((i>='a' and i<='z' )):
                str = str + i
        print("Yes" if str==str[::-1] else "No")
        
a = Solution()
input = "A man, a plan, a canal: Panama"
input = input.lower();
a.isPalindrome(input)