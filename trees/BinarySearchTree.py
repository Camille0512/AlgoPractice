import pandas as pd

LEFT = 1
RIGHT = 2

class BST:
    def __init__(self):
        self.root = None
        self.curval = None
        self.parent = None
        self.left = None
        self.right = None
        self.stage = 0
        self.treeGraph = {}
        self.leftlist = []
        self.rightlist = []

    def createRoot(self, inputList):
        sortedList = self.quickSort(inputList)
        rootInd = int(len(sortedList)/2)+1
        rootVal = sortedList[rootInd]
        self.curval = rootVal
        self.leftlist = inputList[:rootInd]
        self.rightlist = inputList[rootInd+1:]

        if self.stage==0: self.root = self.curval
        self.treeGraph[self.stage] = {
            'root': self.root,
            'level': self.stage,
            'self value': self.curval,
            'left node': self.left,
            'right node': self.right,
        }

    def quickSort(self, inputList):
        indicator = inputList[-1]
        leftside = []
        rightside = []
        for i in inputList:
            if i > indicator:
                rightside.append(i)
            else:
                leftside.append(i)
        return self.quickSort(leftside) + [indicator] + self.quickSort(rightside)

    def createChildren(self, inputList, direction):
        if len(inputList)==1:
            self.treeGraph[self.stage]['left node'] = inputList[0]

        if len(inputList)>1:
            sortedList = self.quickSort(inputList)
            ind = int(len(inputList)/2) + 1
            if direction == LEFT:
                self.treeGraph[self.stage]['left node'] = ind
            leftside = inputList[:ind]
            rightside = inputList[ind+1:]
            return leftside, rightside
