import pandas as pd
data={
       "students":[2000,2007,4000,3700,1000,2500,3000],
       "faculty":  [200,210,  300, 300,100,240,260],
       "year":     [2014,2015,2016,2017,2018,2019,2020],
       "placement":[1800,1900,1000,400,1000,1750,2800]
     }
df=pd.DataFrame(data)
print(df)
print(df[["year","students","placement"]]) #year wise total and placed students
df["sf"]=df["students"]+df["faculty"]
print(df)
print(df.sum())
print(df.columns)
print(df.students)
print(df.iloc[2])  #data at index position passed(index)
print(df[(df.faculty==300) | (df.placement>=500)])

from pylab import *
#plotting graph
#df.hist()
#show()
#df[["year","placement"]].hist()
#show()
p=df["placement"]
y=df["year"]
bar(y,p)  #year wise placements
#show()
df.plot("year","placement",kind="pie")
show()
df.plot("year","placement",kind="bar")
show()





