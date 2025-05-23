import pandas as pd
from pylab import *

data={
      "students":[2000,2007,4000,1000,2500,3000,3700],
      "faculty":[200,210,239,403,240,300,320],
      "year":[2014,2015,2016,2017,2018,2019,2020],
      "placement":[1800,1900,1500,500,1000,1750,2800]

        }
df=pd.DataFrame(data)
print(df)
print(df[["year","students","placement"]])
print("*"*50)
df["sf"]=df["students"]+df["faculty"]
print(df)

print("+"*50)

print(df.sum())
print("+"*50)
print(df.columns)

print("-"*50)

print(df.students)

print("-"*50)

print(df.iloc[2])

print("^"*60)


print(df[(df.faculty==300) & (df.placement>=500)])

#df[["year","students"]].hist()
#show()
'''
p=df["placement"]
y=df["year"]
bar(y,p)
show()
'''
# for direct with pandas
df.plot("year","placement",kind="bar")
show()

df.plot("year","placement",kind="pie")
show()