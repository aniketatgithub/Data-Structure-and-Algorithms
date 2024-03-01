def search( nums, target):
    l,r =0, len(nums)-1
    while(l<=r):
        m = (l+r)//2
        print(m)
        #equal 
        if(nums[m]== target):
            return m
        #left
        if(nums[m]>=nums[l]):
            if(nums[l] <= target and nums[m] >= target ):
                r = m - 1
            else:
                l = m + 1
        #right
        else:
            if(nums[r] >= target and nums[m] <= target):
                l = m + 1
            else : 
                r = m  - 1
print(search([4,5,6,7,0,1,2],0))