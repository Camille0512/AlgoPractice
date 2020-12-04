# class KMPAlgo:
#     def __init__(self):
#         pass
#
#     def match(self, inputStr, pattern):
#         next_array = self.const_next(pattern)
#         i, j = 0, 0
#         comp = False
#         while i < len(inputStr):
#             print("i:{} {} j:{} {}".format(i, inputStr[i], j, pattern[j]))
#             if inputStr[i] == pattern[j]:
#                 comp = True
#             else:
#                 i += 1
#
#             if comp and i<len(inputStr) and j<len(pattern):
#                 if inputStr[i] == pattern[j]:
#                     i += 1
#                     j += 1
#                     if j == len(pattern):
#                         return (i-j, i)
#                 else:
#                     j = next_array[j]
#         return (-1, -1)
#
#     def const_next(self, pattern):
#         next_array = [0, 0]
#         pattern = " " + pattern
#         i, j = 1, 0
#         while i < len(pattern):
#             if j==0 or pattern[i]==pattern[j]:
#                 i += 1
#                 j += 1
#                 next_array.append(j)
#             else:
#                 j = next_array[j]
#         return next_array[1:]

class KMPAlgo:
    def __init__(self):
        pass

    def match(self, inputStr, pattern):
        nextArray = self.const_next(pattern)

        i, j = 0, 0
        while i < len(inputStr):
            if inputStr[i] == pattern[j] and j < len(pattern):
                i += 1
                j += 1
            elif inputStr[i] != pattern[j] and j != 0:
                j = nextArray[j-1]
            elif inputStr[i] != pattern[j] and j == 0:
                i += 1

            if j == len(pattern): return (i-j, i)
        return (-1, -1)


    def const_next(self, pattern):
        i, j = 1, 0
        nextval = [0]

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
                j += 1
                nextval.append(j)
            elif j != 0 and pattern[i] != pattern[j]:
                j = nextval[j - 1]
            else:
                i += 1
                nextval.append(j)
        print(nextval)
        return nextval


if __name__=="__main__":
    tar = "abcdabcxabcdabcabcd"
    pattern = "abcdabca"
    kmp = KMPAlgo()
    res = kmp.match(tar, pattern)
    print("The pattern in the string start from {} to {}".format(res[0], res[1]))
    print("Substring:{} Equal?: {}".format(tar[res[0]:res[1]], tar[res[0]:res[1]]==pattern))
