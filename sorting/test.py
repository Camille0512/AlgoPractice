import pandas as pd
import numpy as np

student = pd.DataFrame(
    [['3', 'Creatiive Thinking', 'female', 'Alice'],
['4', 'Creatiive Thinking', 'male', 'Bob'],
['4', 'Code with Python', 'female', 'Kelly']], columns=['Grade level', 'Program', 'Gender', 'Name']
)

print(student)
pivot = pd.pivot_table(student[['Name','Gender']], index='Name', columns="Gender", aggfunc=np.count_nonzero)
print(pivot)