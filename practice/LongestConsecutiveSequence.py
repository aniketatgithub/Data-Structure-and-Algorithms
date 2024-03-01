def LongestSequence(list):
    if len(list) == 0:return 0
    if len(list) == 1:return 1

    length = 0
    maxlen = 0
    i =0
    lenoflist = len(list)
    while i < lenoflist:
        thenum = list[i]-1
        if(not(thenum in list)):
            length = 1
            num = list[i] + 1
            while((num) in list):
                length+=1
                num += 1
                maxlen = max(length, maxlen) 
        i+=1
    return (maxlen)

print(LongestSequence([0]))
