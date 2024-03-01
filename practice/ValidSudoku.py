
# def searchBox(inputList,abbrRow,abbrCol):
#     numsCount3= [0]*9
#     for i in range(0,10):
#         if(int(i)/3 == abbrRow):
#             for j in range(0,10):
#                 if(int(j)/3 == abbrCol):
#                     numsCount3[int(inputList[i][j])-1] = +1
#     for i in numsCount3:
#         if(numsCount3[i] > 1 ): return False

def isValidSudoku(inputList):
    isRow = [set() for i in range(9)]
    isCol = [set() for i in range(9)]
    isBox = [set() for i in range(9)]

    # [set() set() set() set() set() set() set() set() set()]
    for r in range(9):
        for c in range(9):
            if inputList[r][c] == '.':
                continue

            number = inputList[r][c] 
            # number = 8
            boxNum = (r // 3) * 3 + (c // 3)

            # Condition to check if the number is present in the row or not or column or not or box or not
            if number in isRow[r] or number in isCol[c] or number in isBox[boxNum]:
                return False

            # If the number is not present in the row, col or box, this means that the number is
            # not present. Hence, we add the number in the row, col and box
            isRow[r].add(number)
            isCol[c].add(number)
            isBox[boxNum].add(number)
    
    return True



            






    # result = True
    # numsCount= [0]*9
    # for z in range(0,9):
    #     for i in inputList[0]:
    #         if i != ".":
    #             i1 = int(i)
    #             print(i1-1)
    #             numsCount[i1-1] += 1
    #     for num in numsCount: 
    #         if num>1 : return False 
    #     numsCount.clear()

    # numsCount2= [0]*9
    # for z in range(0,10):
    #     for row in inputList:
    #         for i in row[0]:
    #             if not(i == ".") : numsCount2[int(i)-1] += 1
    #     for i in numsCount2 : 
    #         if i>1 : return False
    #     numsCount2.clear()
    
    # return (searchBox(0,0))


    # return True
    


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))