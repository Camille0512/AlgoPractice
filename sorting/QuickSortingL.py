class quicksort:
    def QuickSortWithPivot(self, target_list: list):
        if len(target_list)<=1: return target_list
        pivot = target_list.pop(-1)
        left_list = []
        right_list = []
        for i in target_list:
            if i < pivot:
                left_list.append(i)
            else:
                right_list.append(i)
        return self.QuickSortWithPivot(left_list) + [pivot] + self.QuickSortWithPivot(right_list)


if __name__=="__main__":
    tarSortList = [3,1,8,6,9,4,2,5]
    qs = quicksort()
    newList = qs.QuickSortWithPivot(target_list=tarSortList)
    print(newList)

from datetime import datetime
from pytz import timezone
a = datetime.now().hour
print(a, type(a))
# tz = timezone("Asia/Shanghai")
tz = timezone("UTC")
print(datetime.now(tz))