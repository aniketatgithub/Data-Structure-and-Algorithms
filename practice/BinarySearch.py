def binarysearch(listofNums, target,start,end):
    if len(listofNums) == 0: return
    else: 
        mid = (start + end)//2
        if( listofNums[mid] == target ):
            return mid
        elif(listofNums[mid] > target):
            return binarysearch(listofNums, target,start,mid-1 )
        else : 
            return binarysearch(listofNums, target,mid+1,end )
print(binarysearch([1,2,3,4,5,6,7,8],2,0,7))