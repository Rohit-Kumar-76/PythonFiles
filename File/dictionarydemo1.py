persons={
         'user1':'user1@123','user2':'user2@123','user3':'user3@123',
         'user4':'user4@123','user5':'user5@123','user6':'user6@123'
        }
#print(persons[0]) #invalid
print(persons["user2"]) #valid
print("All users List:")
for user in persons:
    print(user,"=>",persons[user])

'''   
marks={"Math":65,"Eng":75}

students={
         "Amit":{"Math":65,"Eng":75}
         }

students["Amit"]["Eng"]=input()
'''
print("-"*50)
print(persons.items())
print(persons.keys())
print(persons.values())
print("-"*50)
#update operation
dic2={}  #empty dictionary
dic2["user7"]="user7@123"
dic2.update(persons)
print(dic2)

print("-"*50)
#delete operation
'''
username=input("username to be deleted:")
#dic2.pop("user8")
if username in dic2:
    dic2.pop(username)
    print("user deleted")
else:
    print("invalid username")
'''
dic2.popitem()
dic2.popitem()
dic2.popitem()
print("Updated Data:")
print(dic2)






