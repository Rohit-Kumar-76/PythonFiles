str1="this is string handling using python"

#print("string length:",len(str1))
#print("frequency of i:",str1.count("i"))
print("Enoded value:",str1.encode("utf-8"))
print("Enoded value:",str1.encode("utf-16"))
print("Enoded value:",str1.encode("utf-32"))
print("index of i:",str1.index("i")) #will give first occurence position
print("second index of i:",str1.index("i",3)) #will give second occurence position

str1="abcde"
print(min(str1))
print(max(str1))

str1="this is string handling using python"
str2=str1.replace("i","I")
print(str2)

print(str2.upper())
print(str2.title())
print(str2.capitalize())
print(str2.lower())
print(str2.startswith("thIs"))
print(str2.endswith("Python"))

print("*"*50)
str3="  astric patna  "
print(len(str3))  #16

str4=str3.strip()
print(str3)
print(str4)
print(len(str4)) #12

#using split function
#cities="Patna Delhi Mumbai Lucknow Kolkata Ranchi"
cities="Patna,Delhi,Mumbai,Lucknow,Kolkata,Ranchi"
#citylist=cities.split()
#citylist=cities.split(",")
citylist=cities.split(",",3)
print(citylist)


















