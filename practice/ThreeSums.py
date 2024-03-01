

# BRUTEFORCE: (Half worked)
# def ThreeSums(list1):
#     list2 = []
#     listOfvisited = []
#     for number in range(len(list1)):
#         if(list1[number ] not in listOfvisited):
#             target = 0 - list1[number]
#             if(twoSums(list1,number, target)!= None):
#                 sub_list = [[list1[number]]+twoSums(list1,number, target)]
#             list2.extend(sub_list)
#             sub_list = []
#             listOfvisited.append(list1[number])
#     return list2
    
# def twoSums(list1,index,target):
#     print(target)
#     dict = {}
#     for i in range (len(list1)) : 
#         if(index != i ):  
#             print("Index" + str(i))
#             diff = target - list1[i]
#             if(diff in dict) :
#                 return([list1[i],diff])
#             dict[list1[i]]=i

def ThreeSums(list1):
    resultList = []
    sorted_list = sorted(list1)
    for number,index in enumerate (sorted_list):
        if(index > 0):
            if number == sorted_list[index-1]: continue
        l,r = index + 1, len(list1)-1
        sum = number + sorted_list[l] + sorted_list[r]
        if(sum < 0) : l+=1 
        elif (sum>0): r-=1 
        else : resultList.append([sum,sorted_list[l],sorted_list[r]])
    return resultList



    

nums = [-1,0,1,2,-1,-4]
print(ThreeSums(nums))
