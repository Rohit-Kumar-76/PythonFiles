users=dict()
limit=int(input("How mny users  you want to add:"))
for i in range(limit):
    uname=input("Enter name for user"+str(i+1)+":")
    mobile=input("Enter mobile no for user"+str(i+1)+":")

    users[uname]=mobile


print("registered users are:")
print(users)
