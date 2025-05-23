#users={}
users=dict() #empty dictionary
limit=int(input("How many users you want to register?"))

for i in range(limit):
    uname=input("Enter name for user "+str(i+1)+":")
    mobile=input("Enter mobile no for user"+str(i+1)+":")
    users[uname]=mobile
          #key   value

print("Registered users are:")
print(users)



