year=int(input("enetr a year"))
if (year%400)==0 :
     print(year," is leap year")
elif year % 100==0:
    print(year," is not leap year")
elif year % 4==0:
     print(year," is leap year")
else:
    print(year," is not a leap year")