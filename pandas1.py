import pandas as pd

#Series with default index
series=pd.Series(list("98765"))
#print(series)
series=pd.Series(tuple("abcdef"))
#print(series)
#Series with index
series=pd.Series([9,8,7,6,5],
				 index=["*","**","***","****","*****"])
#print(series)
#print(series[["*","***"]])
#print(series["*"])


#Series with index and incomplete data
series = pd.Series({1:10,2:20,4:30},
				   index = [1,2,3,4])
#print(series)
#print(series*4)
#print(series+4)



#working with dataframe

data={'country':['INDIA','USA',
				 'INDIA','USA'],
	'Year':[2010,2010,2012,2012],
	'Population':[20,28,32,38]}
print(data)
print("*"*50)
dataFrame=pd.DataFrame(data)
#print(dataFrame)
#Adding new column
dataFrame['GDP'] = [ 6.3, 5.7, 7.8, 5.5 ]
print(dataFrame)
print("*"*50)
print(dataFrame["GDP"])
print("\nMin GDP:",dataFrame['GDP'].min())
print("\nMax GDP:",dataFrame['GDP'].max())
print("\nSum of GDP:",dataFrame['GDP'].sum())
print("\nMean of GDP:",dataFrame['GDP'].mean())
print("\nMedian of GDP:",dataFrame['GDP'].median())
print("\nCount of GDP:",dataFrame['GDP'].count())
print("\nHead 2 of GDP:\n",dataFrame['GDP'].head(2))
print("\nTail 2 of GDP:\n",dataFrame['GDP'].tail(2))

print("Descrice Result:")
print(dataFrame.describe())







