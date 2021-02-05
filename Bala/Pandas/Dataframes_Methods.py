import numpy as np
import pandas as pd

print('\n')
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
print(df)

print('\nitertuples')
for row in df.itertuples():
    print('row: ', row)

print('\nitems')
for label,content in df.items():
    print('Label   : ', label)
    print('Content : ', content)

print('\niteritems')
for key,value in df.iteritems():
    print('Key   : ', key)
    print('Value : ', value)


print('\niterrows')
for row_index,row in df.iterrows():
   print('row index: ', row_index)
   print('row', list(row.values))
