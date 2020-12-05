from random import randint
from InsertionSort import InsertionSort

class bucketSort(InsertionSort):
    '''
    The bucket sort is usually used in the situation that the range of the disorder list given.
    '''
    def __init__(self):
        super(InsertionSort, self).__init__()
        self.bucket = []
        self.res = []

    def clear_items(self):
        self.bucket.clear()
        self.res.clear()

    def bucket_sort(self, rawlist, start, end):
        '''
        Bucket sort function.
        :param rawlist: The input disordered list.
        :param start: The start range of the list, also the minimum number of the list. It can be a float or negative.
        :param end: The end range of the list, also the minimum number of the list. It can be a float or negative.
        :return: Sorted list
        '''
        self.clear_items()
        unit = int(end - start) + 1
        self.bucket = [[""] for i in range(unit)]
        for i in rawlist:
            index = int(i) - start
            if self.bucket[index][0] == "":
                self.bucket[index] = [i]
            else:
                self.bucket[index].append(i)

        for i in self.bucket:
            if i[0] != "":
                sublist = self.insertion_sort(i)
                self.res += sublist

        return self.res

if __name__=="__main__":
    testlist = [[randint(1, 50) for i in range(10)] for j in range(3)]
    bks = bucketSort()
    for t in testlist:
        print("raw list:", t)
        res = bks.bucket_sort(t, 1, 50)
        print("sorted list:", res, '\n')

