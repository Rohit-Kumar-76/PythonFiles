import pandas as pd
data={'COUNRTY':['INDIA','USA','INDIA','USA',],
                                                'YEAR':[2010,2012,2011,2013],
                                                'population':[20,28,32,38]


}
print(data)
print("*"*50)
dataFrame=pd.DataFrame(data)
print(dataFrame)
# for ADDING new coloum name
dataFrame['GDP']=[6.3,5.7,7.8,8.2]
print(dataFrame)

print("*"*50)

print("\nMin GDP:",dataFrame['GDP'].min())
print("\nMax GDP:",dataFrame['GDP'].max())
print("\nSum of  GDP:",dataFrame['GDP'].sum())
print("\nMean of GDP:",dataFrame['GDP'].mean())
print("\nmedian of GDP:",dataFrame['GDP'].median())
print("\nCount of GDP:",dataFrame['GDP'].count())
print("\nHead of  GDP:",dataFrame['GDP'].head(2))
print("\nTail of  GDP:",dataFrame['GDP'].tail(2))

print("Describe result ")
print(dataFrame.describe())
