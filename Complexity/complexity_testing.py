from random import randint
from datetime import datetime

class squareNums:
    def __init__(self):
        self.res = 1

    def clear(self):
        self.res = 1

    def square01(self, num, times):
        '''
        Calculate the square of a given number. Using a for loop, time complexity: O(n).
        :param num: A given target number.
        :param times: The times that the number should be squared.
        :return: Store the result of the squared number.
        '''
        self.clear()
        for i in range(times):
            self.res *= num

    def square02(self, num, times):
        '''
        Calculate the square of a given number. Using recursion, time complexity: O(n).
        :param num: A given target number.
        :param times: The times that the number should be squared.
        :return: The result of the squared number.
        '''
        self.clear()
        if times == 0: return 1
        return self.square02(num, times-1) * num

    def square03(self, num, times):
        '''
        Calculate the square of a given number. Using recursion, tree like, time complexity: O(n).
        :param num: A given target number.
        :param times: The times that the number should be squared.
        :return: The result of the squared number.
        '''
        self.clear()
        if times == 0: return 1
        t = int(times / 2)
        if times % 2 == 1: return self.square03(num, t) * self.square03(num, t) * num
        return self.square03(num, t) * self.square03(num, t)

    def square04(self, num, times):
        '''
        Calculate the square of a given number. Using recursion, recurse ahead, time complexity: O(log(n)).
        Recurse in a half way, just like counting the square value of a square value recursively.
        :param num: A given target number.
        :param times: The times that the number should be squared.
        :return: The result of the squared number.
        '''
        self.clear()
        if times == 0: return 1
        newnum = self.square04(num, int(times / 2))
        if times % 2 == 1: return num * newnum * newnum
        return newnum * newnum

    def timeCounter(self, funcNum, num, times):
        '''
        Count the time consumed by different square functions.
        :param funcNum: The function number, string style, formatted in "0*".
        :param num: A given target number.
        :param times: The times that the number should be squared.
        :return: Return the result of the square function. Print the time consumed by the function.
        '''
        start = datetime.now()

        if funcNum == '01':
            start = datetime.now()
            self.square01(num, times)
        elif funcNum == '02':
            start = datetime.now()
            self.res = self.square02(num, times)
        elif funcNum == '03':
            start = datetime.now()
            self.res = self.square03(num, times)
        elif funcNum == '04':
            start = datetime.now()
            self.res = self.square04(num, times)

        end = datetime.now()
        timeDiff = (end - start).microseconds
        print("The square{} function consumed {} microseconds".format(funcNum, timeDiff))

        return self.res



if __name__=="__main__":
    test = [randint(1, 10) for i in range(5)]
    sn = squareNums()
    s = 10000
    for t in test:
        res1 = sn.timeCounter("01", t, s)
        # res2 = sn.timeCounter("02", t, s)
        res3 = sn.timeCou,nter("03", t, s)
        res4 = sn.timeCounter("04", t, s)
        print(" ")
        # print("raw num:{} times:{} res1:{} res3:{} res4:{}\n".format(t, s, res1, res3, res4))