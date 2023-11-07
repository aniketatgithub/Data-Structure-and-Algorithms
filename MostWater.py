#Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# BRUTEFORCE
# def MostWater(heights):
#     maxArea = 0
#     selectedindex = -1
#     for height in heights:
#         selectedHeight = height
#         selectedindex += 1
#         for secondIndex in range(selectedindex+1,len(heights)-1):
#             actualHeight = min(selectedHeight,heights[secondIndex])   
#             actualWidth = secondIndex - selectedindex 
#             maxArea = max(maxArea,actualHeight * actualWidth)
#     return maxArea

def MostWater(heights):
    maxArea = 0
    left = 0
    right = len(heights)-1

    while left < right:
        height = min(heights[right], heights[left])
        width = right - left 
        
        maxArea = max(maxArea,height * width)
        # maxArea = max(maxArea, (right - left) * min(heights[right], heights[left]))
        if(heights[left] >= heights[right]):
            right -= 1
        else:
            left += 1
    return maxArea


print(MostWater([2,1,1,2]))


