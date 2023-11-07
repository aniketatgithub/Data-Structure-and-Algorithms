#optimised version
def numOfhours(pilesize,b):
    hoursadded = 0
    while(pilesize > 0):
        pilesize = pilesize - b
        hoursadded += 1
    return hoursadded
def minEatingSpeed(piles, hr) :
    min1 = max(piles)
    l = min(piles)
    h = max(piles)
    while(l<=h):
        totalH = 0
        m = (l + h)//2
        for i in range(0,len(piles)):
            totalH +=  numOfhours(piles[i],m)
        if(totalH==hr):
            min1 =  m
            h = m-1
        elif(totalH>hr):
            l = m+1
        else:
            min1 = m
            h = m-1
    return min1
            
# #this is another approach that works 
# def canEatAll(piles, K, H):
#     total_hours = 0
#     for pile in piles:
#         total_hours += -(-pile // K)  # This is equivalent to ceiling(pile/K)
#     return total_hours <= H

# def minEatingSpeed(piles, H):
#     # The maximum possible speed is the maximum pile size
#     max_speed = max(piles)
#     for K in range(1, max_speed + 1):
#         if canEatAll(piles, K, H):
#             return K
#     return max_speed

# Example

piles = [30,11,23,4,20]
H = 6
print(minEatingSpeed(piles, H)) 

