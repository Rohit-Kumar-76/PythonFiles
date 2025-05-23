math=int(input("enter your maths marks"))
eng=int(input("enter your  English marks"))
bio=int(input("enter your  Bio marks"))
chy=int(input("enter your  chy marks"))
phy=int(input("enter your phy  marks "))
total=math+eng+bio+chy+phy
grade=total/500*(100)
if grade< 50:
    print("Fail")
elif grade >=50 and grade <60:
     print("c")
elif grade >=60 and grade < 70:
     print("B")
elif grade >= 70 and grade < 80:
     print("B+")
elif grade >=80 and grade < 90:
     print("A")
elif grade >= 90 :
         print("A+")