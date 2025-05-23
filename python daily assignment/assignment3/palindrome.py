n=int(input("enetr any palindrome no"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(" palindrone")
else:
    print(" not paindrone")