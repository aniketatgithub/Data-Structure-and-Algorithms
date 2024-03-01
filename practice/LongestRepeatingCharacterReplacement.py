# def longestRepeatingCharacter(chars , k ) : 
#     longestLength = 0
#     characterLength = len(chars)
#     for index,char in enumerate (chars) :
#         length,knum = 0,0
#         while((index < characterLength-1) and (chars[index] == chars[index+1] or knum <= k) ):
#             if((chars[index] != chars[index+1])):
#                 knum += 1
#             if( (index < characterLength-1)):
#                 index += 1
#             length += 1
         
#             longestLength = max(longestLength, length)
#             if(index == characterLength-1):
#                 if(chars[index-1] == chars[index]):
#                     longestLength+=1
#     return longestLength
def longestRepeatingCharacter(s, k):
    hashmap1 = {}
    l =0 
    maxlen = 0
    for r in range(len(s)):
        hashmap1[s[r]] = 1 + hashmap1.get(s[r],0)
    
        while(r - l +1 - max(hashmap1.values()) > k):
            hashmap1[s[l]] -=   1
            l+=1
        
        maxlen = max(maxlen,r-l+1)

    return maxlen


    # for index in range(0, len(inputStr)):
    #     hashmap[inputStr[index]] = 1 + hashmap.get(index,0)

    # l,r =0,0
    # while(l - r + 1 <= k ):
    #     r+=1
    # l-=1
    


chars =  "ABAB"
k = 2
print(longestRepeatingCharacter(chars,k))