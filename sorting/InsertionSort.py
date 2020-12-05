from random import randint
class InsertionSort:
    def __init__(self):
        pass

    def swap_sort(self, rawlist):
        '''
        From small to large.
        :param rawlist: Input disordered list.
        :return: Ordered list from small to large.
        '''
        for e, i in enumerate(rawlist[1:]):
            while e >= 0:
                if i < rawlist[e]:
                    rawlist[e+1] = rawlist[e]
                    rawlist[e] = i
                else:
                    break
                e -= 1
        return rawlist

    def insertion_sort(self, rawlist):
        '''
        From small to large.
        :param rawlist: Input disordered list.
        :return: Ordered list from small to large.
        '''
        for e, i in enumerate(rawlist[1:]):
            key = i
            while e >= 0 and key < rawlist[e]:
                rawlist[e+1] = rawlist[e]
                e -= 1
            rawlist[e + 1] = key
        return rawlist


if __name__=="__main__":
    testlist = [[randint(1,50) for i in range(10)] for j in range(3)]
    # testlist = [[5,2,4,3,1]]
    print("testlist:\n", testlist)
    iss = InsertionSort()
    for t in testlist:
        res = iss.insertion_sort(t)
        print(res, '\n')
