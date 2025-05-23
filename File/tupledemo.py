course_list=("Python","C","C++","Java")

print(course_list)

print("Courses are:")
for course in course_list:
    print(course)

print("--------------------------")
print(course_list[0]) #Python
print(course_list[-1]) #Java
print(course_list[1:3]) # c,c++
print(course_list[:3])  #
print(course_list[2:])  #
print(course_list[::-1])#
#course_list[0]="C#"  #invalid ,not allowed
my_tuple=(10,20,[30,40,50],60,70,[80,90,10])
print("------------------------")
print(my_tuple)
# my_tuple[0]=120
# my_tuple[2]=200
my_tuple[2].append(60)
print("------------------")
print(my_tuple)
