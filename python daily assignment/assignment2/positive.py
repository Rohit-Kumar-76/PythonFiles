x=int(input())
if x<0:
    print("negative")
elif x==0:
    print("zero")
else:
    print("postive")
#another way

if x>0:
    print("positive no")
elif x==0:
    print("zero")
else :
    print("negative no")
#way2
print("postive") if x>0 else print("negative")