import pandas as pd
#load data from csv
emp=pd.read_csv("employees.csv")
#print(emp)

'''
print(emp.columns)
print(emp.First_Name)
print(emp.Employee_Id.head(10))
print(emp.iloc[20])
print(emp.iloc[20].First_Name)
'''
dept=pd.read_csv("Departments.csv",
                 index_col=0)
#print(dept)

emp_dept=pd.merge(emp,dept,
                  how="inner",
                  on="Department_Id")
#print(emp_dept)
#print("*"*50)
#print(emp_dept.head(5))
#print(emp_dept[["Employee_Id","First_Name","Department_Name"]].head(5))


loc=pd.read_csv("Locations.csv", index_col=0)
#print(loc)
#print(dept.columns)
#print(loc[["City","State_Province"]])


dept_loc=pd.merge(dept,loc,how="inner", on="Location_Id")

#print(dept_loc[["Department_Name","City"]])


pd.set_option("display.max_rows",10)
pd.set_option("display.max_columns",4)
pd.set_option("display.max_colwidth",2000)
pd.set_option("display.width",2000)
print(dept_loc)

'''
g=emp.groupby(["First_Name","Hire_Date"])
print(g.first())
'''
#print(emp)