stud = {}

mrk = []

print("ENTER ZERO NUMBER FOR EXIT !!!!!!!!!!!!")

print("ENTER STUDENT INFORMATION ------------------------ ")

while True :

    rno = int(input("enter roll no.. :: -- "))

    if rno == 0 :

       break

    else:

        for i in range(3):

          print("enter marks ",i+1," :: -- ",end = " ")

n = int(input())

mrk.append(n)

stud[rno] = mrk

mrk = []

print("Records are ------ ",stud)

print("\nRollNo\t Mark1\t Mark2\t Mark3\t Total")

tot = 0

for r in stud:

    print(r,"\t",end=" ")

    for m in stud[r]:

        tot = tot + m

        print(m,"\t",end=" ")

print(tot)

tot = 0