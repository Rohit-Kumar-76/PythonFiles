import pandas as pd
emp=pd.read_csv("employees.csv")
print(emp)
'''
print(emp.columns)
print(emp.First_Name)
print(emp.Employee_Id.head(10))
print(emp.iloc[20])
print(emp.iloc[20],First_Name)

'''
dept=pd.read_csv("Departments.csv",
                 index_col=0)
print(dept)

emp_dept=pd.merge(emp,dep,
                  how="inner",
                  on="Department_Id")
print(emp_dep)
print("*"*40)
print(emp_dep.head(5))
print(emp_dep[["Employee_Id","First_Name","Deprtment_Name"]].head(5))


#pd.set_option("display.max_rows",10)
#pd.set_option("display.max_columns",4)
#pd.set_option("display.max_colwidth",2000)
#pd.set_option("display.width",2000)
#print(dept_loc