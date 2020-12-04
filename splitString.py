def splitString(InpStr):
    StrList = InpStr.split(" ")
    for e, i in enumerate(StrList):
        StrList.insert(e, i.strip(",").strip('”').strip("“").strip(".").lower())
        StrList.remove(i)
    return StrList

def sortByVal(InpDict):
    maxVal = max(InpDict.values())
    newList = []
    for i in reversed(range(maxVal)):
        for j in InpDict:
            if i+1==InpDict[j]:
                newList.append(j+','+str(InpDict[j]))
    return newList

import sys
if __name__ == "__main__":
    # 读取第一行的n
    stringDict = {}
    while True:
        # 读取每一行
        line = sys.stdin.readline().strip()
        if line=="":
            break
        res = splitString(line)
        for i in res:
            if i in stringDict:
                stringDict[i] += 1
            else:
                stringDict[i] = 1
    #print(sortByVal(stringDict))
    newList = sortByVal(stringDict)
    for i in newList:
        print(i)