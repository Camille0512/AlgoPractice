import pandas as pd

a = pd.DataFrame(
    [['a',1],['b',2],['c',3],['d',4]],
    columns=['name','num']
)
print(a)
col = a.columns.values
for i in range(len(a)):
    line = a.iloc[i]
    print("name:{} num:{}".format(line[0], line[1]))