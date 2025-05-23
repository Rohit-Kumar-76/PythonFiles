
#x=-25
#y=~x
#print(y)

x=20
y=5
z=x/y
print(z)

y=6
z=x//y  #floor division
print(z)

x=1234
y=10
z=x%y  # modulous division
print(z)

x=2
y=6
z=x**y
print(z)

#logic to reverse 3 digit number
x=245
rev=0  # for result
#pass-1
rem=x%10   #5
rev=rev*10+rem  #0*10+5=>5
x=x//10   #24
#pass-2
rem=x%10   #4
rev=rev*10+rem  #5*10+4=>54
x=x//10   #2
#pass-3
rem=x%10   #2
rev=rev*10+rem  #54*10+2=>542
x=x//10   #0
print(rev)













