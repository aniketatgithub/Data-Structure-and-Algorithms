def partition(start,end,lnums):
    if (len(lnums) == 0 or len(lnums) ==1 ):
        return
    else:
        pivot = lnums[end]
        i = start
        k = start -1
        while(i<end):
            if(pivot>lnums[i]):
                k+=1
                lnums[i],lnums[k] = lnums[k],lnums[i]
            i+=1
    k+=1
    lnums[k],lnums[end] = lnums[end],lnums[k]
    return (k)

def quickSort(start,end,lnums):
    pos = partition(start,end,lnums)
    partition(0,pos - 1,lnums)
    partition(pos + 1,end,lnums)
    return (lnums)

lnums = [1,10,9,8,7,6,5]
print(quickSort(0,len(lnums)-1,lnums))