from random import randint

class MergeSort:
    def __init__(self):
        pass

    def merge_lists(self, sublist: list, ascending = True):
        if len(sublist) == 1 or not sublist: return sublist
        mid = int(len(sublist) / 2)
        left = sublist[:mid]
        right = sublist[mid:]
        left = self.merge_lists(left)
        right = self.merge_lists(right)
        if ascending:
            return self.sort_SmallToLarge(left, right)
        else:
            return self.sort_LargeToSmall(left, right)

    def sort_SmallToLarge(self, leftList: list, rightList: list):
        '''
        From the small to the large.
        '''
        res = []
        while leftList and rightList:
            if leftList[0] < rightList[0]:
                res.append(leftList[0])
                leftList.remove(res[-1])
            else:
                res.append(rightList[0])
                rightList.remove(res[-1])
        res += leftList if leftList else rightList
        return res

    def sort_LargeToSmall(self, leftList: list, rightList: list):
        '''
        From the large to the small.
        '''
        res = []
        while leftList and rightList:
            if leftList[0] > rightList[0]:
                res.append(leftList[0])
                leftList.remove(res[-1])
            else:
                res.append(rightList[0])
                rightList.remove(res[-1])
        res += leftList if leftList else rightList
        return res

if __name__ == "__main__":
    testlist = [[randint(1,50) for i in range(10)] for j in range(3)]
    ms = MergeSort()
    for t in testlist:
        newList = ms.merge_lists(t, True)
        print("raw list:", t)
        print('newList: ', newList, '\n')