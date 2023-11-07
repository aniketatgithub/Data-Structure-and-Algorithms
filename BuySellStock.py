import sys
list1 = [7,1,5,3,6,4]
min = sys.maxsize
diff = 0
for i in range(len(list1)):
    min = list1[i] if min > list1[i] else min
    diff = (list1[i] - min) if diff < (list1[i] - min) else diff
print(diff)