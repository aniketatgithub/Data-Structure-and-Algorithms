
def validate(listofargs):
    dict = {"}":"{",
            "]":"[",
            ")":"("}
    

    stack = []
    for i in range(len(listofargs)):
        if(len(stack)!=0 and ( (listofargs[i] in dict.keys())) and (dict[listofargs[i]]==stack[-1])):
                stack.pop()
        else : stack.append(listofargs[i])
    if(len(stack) == 0):
        return True
    else: return False
        




print(validate("({})"))