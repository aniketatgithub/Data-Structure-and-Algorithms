def productExceptSelf(nums):
    result = [0] * len(nums)
    prev = 1
    j =0;
    for i in nums:
        result[j] = prev
        prev = prev * i
        j += 1
    # for i in range(len(result)) : 
    #     print(result[i],end=" ")
    j = len(nums)-1
    prev = 1
    while(j >= 0):
        result[j] = prev * result[j]
        prev = prev * nums[j]
        j-=1
        # print("")
    # for i in range(len(result)) : 
    #     print(result[i],end=" ")
    # for i in range(len(nums)) :
    #     result[i] = result[i] * nums[i]
    return result
        

    


print(productExceptSelf([1,2,3,4]))