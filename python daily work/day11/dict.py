persons={
         'user1': 'user1@123','user2':'user2@123','user3':'user3@123',
         'user4': 'user4@123','user5':'user5@123','user6':'user6@123'
        }
'''
print(persons["user2"])
# after applying for loop , we get key value
print("all user lists:")
for user in persons:
    # it will print user name
    print(user,"=>",persons[user])# it will print all users value
'''

marks={"math":65,"eng":78,"hindi":78}
students={
           "rohit":{"math":65,"eng":75}
         }
students["rohit"]["math"]
print(students)


'''
print("-"*50)
print(persons.items())
print(persons.keys())
print(persons.values())

print("-"*60)
dic2={}
dic2.update(persons)
print(dic2)

dic2["user7"]="user7@123"
dic2.update(persons)
print(dic2)

print("-"*50)
username=input("enetr user name")
if username in dic2:
    dic2.pop(username)
    print(username,"user deleted")
else:
    print("invalid user")

print("-"*60)

dic2.popitem()
dic2.popitem()
print("uppdated data:")
print(dic2)

'''
