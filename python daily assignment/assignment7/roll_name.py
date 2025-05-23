n = int(input("Enter number of students: "))

result = {}

for i in range(n):

    print("Enter Details of student No.", i+1)

    rno = int(input("Roll No: "))

    name = input("Name: ")

    math = int(input("Math: "))
    phy= int(input("phy: "))
    bio= int(input("bio: "))

    result[rno] = [name,[ "math",math,"phy",phy,"bio",bio]]

print(result)

