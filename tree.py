class TreeNode : 
    def __init__(self,data):
        self.data = data
        self.rightNode = None
        self.leftNode = None

    def inverse(self,Topnode):
        if(Topnode is  None):
            return None
        temp = Topnode.leftNode
        Topnode.leftNode = Topnode.rightNode
        Topnode.rightNode = temp
        self.inverse(Topnode.leftNode)
        # print(Topnode.data)
        self.inverse(Topnode.rightNode)

    def findDepth(self,Topnode,count,maxcount):
        if(Topnode is None):
            return maxcount
        else : 
            count = count+1
            if count> maxcount :
                maxcount = count
            maxcount = self.findDepth(Topnode.leftNode,count,maxcount)
            maxcount = self.findDepth(Topnode.rightNode,count,maxcount)
        return maxcount

            

    def inOrderTravelprint(self,Topnode):
        if(Topnode is  None):
            return None
        self.inOrderTravelprint(Topnode.leftNode)
        print(Topnode.data)
        self.inOrderTravelprint(Topnode.rightNode)


zerothNode = TreeNode(0)
firstNode = TreeNode(1)
secondNode = TreeNode(2)
thirdNode = TreeNode(3) 
firstNode.leftNode = zerothNode
firstNode.rightNode =  secondNode
secondNode.rightNode = thirdNode
print(firstNode.findDepth(firstNode,0,0))
# firstNode.inOrderTravelprint(firstNode)