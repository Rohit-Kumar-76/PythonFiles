import pandas as pd
series=pd.Series(list("98765"))
print(series)

series=pd.Series(tuple("abcd"))
print(series)

series=pd.Series([9,8,7,6,5],["*","**","***","****","*****"])
print(series)


se=pd.Series({1:10,2:20,4:30},index=[1,2,3,4])
print(se)

print(se*4)
print(se+5)
print(se-4)
