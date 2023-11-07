#hashmaps
target = 5
list1 = [1,2,3,4,5]
dict = {}
for num in range(len(list1)):
    diff = target - list1[num]
    if(diff in dict):
        print(num,dict[diff])
    dict[list1[num]] = num;
