class MergeSort:
    def __init__(self):
        pass

    def merge_lists(self, sublist: list):
        if len(sublist)==1: return sublist
        if sublist==None: return
        left_list = sublist[:int(len(sublist) / 2)]
        right_list = sublist[int(len(sublist) / 2):]
        left_list = self.merge_lists(left_list)
        right_list = self.merge_lists(right_list)
        return self.sort_list(left_list, right_list)

    def sort_list(self, leftList: list, rightList: list):
        sorted_list = []

        l, r = 0, 0
        while len(leftList) > l and len(rightList) > r:
            if leftList[l] >= rightList[r]:
                sorted_list.append(leftList[l])
                l += 1
            else:
                sorted_list.append(rightList[r])
                r += 1
        if l < len(leftList) and r == len(rightList):
            sorted_list += leftList[l:]
        elif l == len(leftList) and r < len(rightList):
            sorted_list += rightList[r:]

        return sorted_list

if __name__ == "__main__":
    tarSortList = [3, 1, 8, 6, 9, 4, 2, 5, 8, 3, 0, 0.4]
    ms = MergeSort()
    newList = ms.merge_lists(tarSortList)
    print('newList: ', newList)