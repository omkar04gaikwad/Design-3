# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.flatten(nestedList)
        self.size = len(self.res)
        self.idx = 0

    def flatten(self, nestedList):
        for list_ in nestedList:
            if list_.isInteger():
                self.res.append(list_.getInteger())
            else:
                self.flatten(list_.getList())
    
    def next(self) -> int:
        val = self.res[self.idx]
        self.idx += 1
        return val
        
    def hasNext(self) -> bool:
        if self.idx < self.size:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())