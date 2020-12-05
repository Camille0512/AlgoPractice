import sys

# for line in sys.stdin:
#     print(line, end="")

samples = ["{9{0[]}0)", "]}[[[)]]{]}0)", "(09093[452)]", "[)([", "()", "(000)", "([)]", "({0}[)]", "({0[})]"]

formatDict = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def symbol_pairs(inputStr):
    checklist = []
    for i in inputStr:
        if i in formatDict.values():
            checklist.append(i)
        elif i in formatDict.keys() and len(checklist) > 0:
            if checklist[-1] == formatDict[i]:
                return True
            else:
                checklist = []
    return False

for s in samples:
    res = symbol_pairs(s)
    print(s, ": ", res)