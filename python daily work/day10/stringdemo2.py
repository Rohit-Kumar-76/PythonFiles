
x=305454545
y=30
#formatting using % and format chars
print("value of x:%dvalue of y:%d"%(x,y))
print("value of x:%015dvalue of y:%d"%(x,y))
print("value of x:%dvalue of y:%d"%(x,y))
print("value of x:%015dvalue of y:%d"%(x,y))
#formatting using string format method and placeholder
print("*"*25)
print("value of x:{0}value of y:{1}".format(x,y))
print("value of x:{1}value of y:{0}".format(y,x))

print("*"*25)
a1="Python"
a2="Java"
a3="Android"
print("|{:<10}|{:^20}|{:>10}|".format(a1,a2,a3))
print("|{:<10}|{:^20}|{:>10}|".format(a1,a2,a3))
print("|{:<10}|{:^20}|{:>10}|".format("Java","Python","PHP"))
print("|{:<10}|{:^20}|{:>10}|".format("C++","Android","ML"))