def countBits(n):
    # result = []
    # for i in range(0,n+1):
    #        result.append(bin(i).count('1')) 
    # print(result)
    result = [0]
    for i in range (1,n+1):
        result.append(result[int(i/2)] + (i & 1))
    print (result)


countBits(5)